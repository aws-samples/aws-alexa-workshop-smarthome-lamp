const AWSIoT = require('aws-iot-device-sdk');
const QRCode = require('qrcode');

// Change the configuration below
const thingName = 'ratchet';
const iotEndpoint = 'abty4kifln98q-ats.iot.us-east-1.amazonaws.com';
const deviceBindingUrl = 'https://xxxx.com/';

const shadow = AWSIoT.thingShadow({
  keyPath: 'credentials/private.key',
  caPath: 'credentials/rootCA.pem',
  certPath: 'credentials/cert.pem',
  clientId: thingName,
  host: iotEndpoint
});

let clientTokenUpdate;

shadow.on('connect', function () {
  shadow.register(thingName, {}, function () {

    const initState = {
      state: {
        reported: {
          power: "OFF"
        }
      }
    };

    clientTokenUpdate = shadow.update(thingName, initState);

    if (clientTokenUpdate === null) {
      console.log('update shadow failed, operation still in progress');
    }

    console.info('connected to IoT Core...\n');

    console.info('This is the QR Code shipped with the Device:');
    QRCode.toString(`${deviceBindingUrl}?thingName=${thingName}`, {type: 'terminal'}, function (err, string) {
      if (err) throw err;
      console.log(string)
    })
  })

});

shadow.on('delta', function (thingName, stateObject) {
  const desiredPowerState = stateObject.state.powerState;
  const reportedState = {
    state: {
      reported: {
        powerState: desiredPowerState
      }
    }
  };

  shadow.update(thingName, reportedState);

  console.info(`turn ${desiredPowerState} Smart Lamp`)
});

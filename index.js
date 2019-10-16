const AWSIoT = require('aws-iot-device-sdk');
const QRCode = require('qrcode');
const config = require('./config')


console.log('Smart lamp simulator');

const shadow = AWSIoT.thingShadow({
  keyPath: 'credentials/private.key',
  caPath: 'credentials/rootCA.pem',
  certPath: 'credentials/cert.pem',
  clientId: config.thingName,
  host: config.iotEndpoint
});

let clientTokenUpdate;


shadow.on('connect', function () {
  console.log('Connected');  
  shadow.register(config.thingName, {}, function () {

    const initState = {
      state: {
        reported: {
          powerState: "OFF"
        }
      }
    };

    clientTokenUpdate = shadow.update(config.thingName, initState);

    if (clientTokenUpdate === null) {
      console.log('update shadow failed, operation still in progress');
    }

    console.info('connected to IoT Core...\n');

    console.info('This is the QR Code shipped with the Device:');
    let url = `${config.deviceBindingUrl}?thingName=${config.thingName}`
        QRCode.toString(url, {type: 'terminal'}, function (err, string) {
      if (err) throw err;
          console.log(string)
          console.log(`Browse to ${url} to register`)

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

  shadow.update(config.thingName, reportedState);

  console.info(`turn ${desiredPowerState} Smart Lamp`)
});

shadow.on('error', (err) => { console.log(err) });

shadow.on('offline', () => { console.log('Disconnected') })
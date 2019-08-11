1. 章节的排版有问题，在markdown 里面，如果是list 用 * 或者 1. 会显示正确

1. 章节的设置，第一章节为 "Creating "Thing", security policies and certificates", 
后面有出现了 "create thing", "policy" 章节，可以合并成一个章节; 章节标题建议清晰的表达目的
"MQTT pub/sub", "Quick Review" ， "test MQTT pub/sub" 从标题上不清楚这个段落的目标是什么

1. AWS CLI 本实验没有使用场景

1. 文章中无需贴 全部代码，一般只贴 重要代码部分; 会造成文章过长，用户抓不住重点

1. 项目依赖尽量保持独立，不建议全局安装依赖，会存在破坏用户现有环境的可能性

1. 标题是h1， markdown 中是 #。 h2 是 ##, 成递进关系

1. "In the above screenshots, you’ll see a “Connect” menu option." 文字和截图不符，应该是 **Onboard**

1. 过于简单的 AWS Console 操作不需要每一步都截图，关键步骤即可。 文章过长会导致

1. 在选择 IoT 运行platform 的时候，没有考虑到 Windows 用户

1. 选择完 platform 和 Python 之后，不应该出现 img/lab1-4.png 这个截图。。 这个截图是第一步

1. 英文表达过于口语化。。。"Ok so now we’re ready to get started.", "let’s see", "that's it" 英文 technical 文档中，
多于第二人称视角，基本不用 we, I 等表达方式，

1. 使用相对路径， 如[./start.sh](./start.sh), 而不是[https://github.com/lab798/aws-alexa-workshop-smarthome-lamp/blob/master/sample.py](https://github.com/lab798/aws-alexa-workshop-smarthome-lamp/blob/master/sample.py).
项目如果有移动或者rename, 会造成不可访问。 这里由于start.sh 没啥用，直接去掉了

1. Step 8 - Test Shadow 和之前的 test pub/sub 普通的topic 存在冗余。 shadow只是特殊的topic而已。

1. zip 解压出来key 的名称和代码里面的不同，没有说明需要重命名

1. 程序有错误，收到 OFF 指令后，依然上报 ON 状态
 
TIPS: 按那一个按钮，哪个地方需要输入，建议用 `** **` 做粗体，参考下AWS 产品手册，几乎都是这么做的

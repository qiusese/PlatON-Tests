# deploy

部署节点的相关依赖

- node:用于存放部署节点的配置文件,格式说明如下

```yml
collusion: # 共识节点，有时必填
- host: 10.10.8.236 # 节点ip，必填
  username: juzhen  # 节点机器账户，必填
  password: Platon123! # 节点机器密码，必填
  id: 5b068ef1cfeef626d9ad131d08b889002a2f5c7306ff34c3032ad04fcc92fd234d0c7272014068eb998dae2abfe9f10271ed6731963b1cf22ec944abd8fb0f9e # 节点公钥，非必填，最好不填
  nodekey: 3314532da43158885d8db07e0b25dc0c194c8382c4fa5ce8c28a0b7c86cdec16 # 节点私钥，非必填，最好不填，需要与公钥对应
  port: 16789 # p2p端口，非必填，最好填
  rpcport: 6789 # rpc端口，非必填，最好填
  url: http://10.10.8.236:6789 # rpc url，非必填，最好不填
  protocol: ws # 协议，默认为http，非必填，需要使用ws时必填
- host: 10.10.8.237
  username: juzhen
  password: Platon123!
  id: 0bb52ab990a687784d12e8fb8c95a7722c949a9982d5858b370db47ee9595044b7af7a6ddfe9e9423f4acdab92f8c75ebb11bbf9d52cc26b57b83d7b4847218d
  nodekey: 03a07edbbe8bc533ebfb967d248e39146a1f8b92fe8226a19513c689e1f3136d
  port: 16789
  rpcport: 6789
  url: http://10.10.8.237:6789
nocollusion: # 非共识节点，有时必填
- host: 10.10.8.239
  username: juzhen
  password: Platon123!
  protocol: ws
  id: b44dd4483dbbefc8357abcd05b05caad4b6b571371222f45165b6c8d4a17bf20f969cc414d0058439f22f560b6f43a4cc4ca8a1d1f3310512421fdd8233019d7
  nodekey: 0e773fba5f72d49b693b181fbba8e20830c380dbca43a26dccffe1d4b7e56f35
  port: 16789
  rpcport: 6789
  url: ws://10.10.8.239:6789
  ```

- rely:部署依赖的文件
  
   1.bin：platon二进制文件，有改动时需要更新。

   2.keystore：创世文件中写入余额的钱包json文件。

   3.template：创世文件模板和cbft文件模板。

   4.tmp：用于存放测试过程中新生成的文件，如cbft.json。

   5.deploy：部署执行脚本
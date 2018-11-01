# 框架说明
你只需要更改三个文件夹的东西

## 算法文件夹 alg
        你需要按照eg文件夹的格式进行算法的放置，
    main.py文件放置主要算法mainAlg

## restful接口文件夹 api
        你需要按照eg文件夹的格式进行api接口的编写
    main.py中需要放置相关handler,在api文件夹下的
    __init__.py中进行接口的定位

## 测试文件夹 test
        你需要按照eg文件夹的格式来进行单元测试的编写
    文件夹下的文件需要以test开头，主要存放testCase
    test文件夹下的文件会自动识别testCase

## 运行test
    sh runTest.sh

## 运行服务
    sh runServer.sh
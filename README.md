舆情分析项目仓库

## 一些事项

1. `utils`文件夹下是各个功能模块：`.py`文件
2. `templates`文件夹下编辑需要的展示模块，如词云图等，最好一个图一个html文件：`html`文件
3. 不是自己写的东西就不要做改动，只对自己的内容做修改
4. 不要使用依赖扫描工具如`pip freeze`、`pipreqs`等，手动更新`import`模块及其版本
5. 前端项目中，全部使用在线引入的方式引入js模块：[在线cdn引入-国内库资源](https://www.bootcdn.cn/)，[国外库](https://cdn.jsdelivr.net/)
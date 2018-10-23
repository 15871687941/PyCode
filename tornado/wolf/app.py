# coding = utf-8
import tornado
from tornado import web, ioloop, httpserver

# 一个部门， 一个页面
# 业务模块 部门
class MainPageHandle(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')
        # self.write("学习是一个积累的过程")


# 新建一个部门， 创建游戏
class CreateGameHandle(web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.render('index.html')
        self.write("第二个界面")

    def post(self, *args, **kwargs):
        # self.get_argument()
        pass


# 设置
setting = {
    'template_path': 'template',  # 模板路径
    'static_path': 'static'  # 静态路径
}
# 路由系统 分机系统
application = web.Application([
    (r"/", MainPageHandle),
    (r"/create_game", CreateGameHandle)
], **setting)
if __name__ == '__main__':
    # socket服务器 前台
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()

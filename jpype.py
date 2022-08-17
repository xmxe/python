import os
import jpype

# 调用jar包位置
jarpath = os.path.join(os.path.abspath("."), "/home/abc.jar")
# jvm默认位置
defaultJVMPath = jpype.getDefaultJVMPath()
# 自定义jvm路径
jvmPath = 'C:\\Program Files\\Java\\jdk1.8.0_161\\jre\\bin\\server\\jvm.dll'
# jvmPath = '/home/jdk1.8.0_161/jre/lib/amd64/server/libjvm.so'

# 配置jvm并启动
jpype.startJVM(jvmPath,'-ea','-Djava.class.path=%s' % jarpath)
# 加载类到jvm 返回类实例
nseadb = jpype.JClass('com.xmxe.Read')
# jpype.java.lang.System.out.println('hello world')

# 定义java.util.Date类型
date = jpype.java.text.SimpleDateFormat('yyyy-MM-dd HH:mm:ss').parse('2022-01-01 00:00:00')
# 加载jar包中的某个类
mode = jpype.JClass('com.xmxe.RtdbModeEnum')
# 调用接口
response = nseadb.method('aaa',date,mode)
print(response)

jpype.shutdownJVM()
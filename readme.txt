===================================

            Drugs  Mapper

          药品结果选择网页
-----------------------------------
               作者：徐涌盛(CINAC)
	github/chux0519
===================================

介绍：
该网页将药品比对中间结果以网页的形式展示，由用户判断是够匹配正确，正确匹配的结果将会建立一个id与id的映射关系。
该网页使用python编写，要求服务器装好解释器，以及一下几个依赖包：
1.flask
2.MySQLdb
3.SQLAlchemy
4.wtforms
5.xlrd
依赖包安装方法 ：pip install [包名]

==================================================================================

使用说明：
1.该网页依赖于包含‘目标药物’和‘比对药物’的中间结果。（注：以xls形式存储的表格）

==================================================================================

2.目录结构：
./flask:
	59146.xls  config.pyc  db.py   gl.py   openxl.py   readme.txt  target
	config.py  control.py  db.pyc  gl.pyc  openxl.pyc  static      templates

	./static:
		jquery-2.1.4.min.js  show.css  top.png  welcome.css

	./target:
		59146.xls  config_log.txt  sql_log.txt  ziyang20160111.xls

	./templates:
		show.html  sidebar.html  welcome.html

==================================================================================

3.管理员配置说明：
1）.以上目录为工程的目录树，将待处理的中间结果存放在 /flask/target 内（如：
/target/59146.xls			/target/ziyang20160111.xls）

2）.分配任务在数据库中直接添加行即可，数据库mapper，表task即为任务分配表
包含字段：
task_id,middle_result_name,student_name,student_num
task_id 	即为任务号
middle_result_name	即为中间结果的xls文件的名称（文件名前后一定不能包含空格换行符）
studen_name		为学生姓名（暂时未测试中文，编码应该是支持的）
student_num		为学生学号
SQL：INSERT INTO `task` (`task_id`, `middle_result_name`, `student_name`, `student_num`) VALUES ('1', 'target/XXX.xls', 'name', '202020202')

3）.任务分配完成以后，要对所分配的表进行配置，在flask目录下，有一个config.py文件
使用方法：
	python config.py [中间结果名]	[xls文件中“药品ID”的列名]  [参考数据库中“id”的列名]
如下：
	python config.py "tartget/59146.xls" "药品ID" "num"
完成后在mapper数据库中的，task_config表中应该会有一个相关列，即为相关的配置文件
4）.配置成功后运行contro.py即可
	python control.py

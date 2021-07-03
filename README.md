# FlaskMVC

基于Flask框架的快速启动模板

## 数据库准备

```sql
CREATE DATABASE `flask_mvc` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci';
CREATE USER 'flask'@'localhost' IDENTIFIED BY 'flask';
REVOKE ALL ON *.* FROM 'flask'@'localhost';
GRANT ALL PRIVILEGES ON `flask_mvc`.* TO 'flask'@'localhost';
```

运行`model/__init__.py`初始化数据

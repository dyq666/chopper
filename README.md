## 说明

项目名: 海贼王乔巴.

生成一些常见的配置文件.

## 目录结构

- `/template` 一些配置文件的模板, `{}` 中是可设置的变量.

- `/conf` 配置文件生成的位置.

- `gen.py` 将模板转为配置文件的脚本.

## 具体配置文件说明 & 应用

### flaskenv.tmpl

  flaskenv 配置文件.

  - 生成 `python3 gen.py flaskenv --app {app} --port {port}`

  - 复制 `cp conf/flaskenv.conf {your_path}/.flaskenv`

### git.tmpl

  GIT 配置文件, 其中有很多常用的 alias 和大量的注释.

  - 生成 `python3 gen.py git --name {name} --email {email}`

  - 复制 `cp conf/git.conf ~/.gitconfig`

### gitignore.tmpl

  个人常用的 Python 语言 .gitignore.

  - 复制 `cp template/gitignore.tmpl <your_path>/.gitignore`

### ipython_shell.tmpl

  一个可预置变量的 Ipython, 使用方式为: `phthon shell.py`.

  - 复制 `cp template/ipython_shell.tmpl <your_path>/shell.py`

## 代码

### 如何增加新的模板以及生成脚本

- 在 template/ 中创建一个新的文件 `{foo}.tmpl`

- 在 `gen.CmdType` 中新增一个常量, 以及 `CmdType.Vars` 设置模板中对应的变量名

- 在 `gen.py` 中写一个 sub parser

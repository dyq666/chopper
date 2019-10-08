## 说明

生成一些常见的配置文件

## 目录结构

- `/template` 一些配置文件的模板, `{}` 中是一些生成配置文件时的变量

- `/conf` 最终配置文件生成的位置

- `gen.py` 将模板转为配置文件的脚本

## 具体配置文件说明 & 应用

### flaskenv.tmpl

  - 生成配置文件 `python3 gen.py flaskenv --app <app> --port <port>`

  - copy 复制文件 `cp conf/flaskenv.conf <your_path>/.flaskenv`

### git.tmpl

  - 生成配置文件 `python3 gen.py git --name <name> --email <email>`

  - link 配置文件 `ln -s conf/git.conf ~/.gitconfig`

### gitignore.tmpl

  - `cp template/gitignore.tmpl <your_path>/.gitignore`

### ipython_shell.tmpl

  - `cp template/ipython_shell.tmpl <your_path>/shell.py`

### makefile.tmpl

注意 Makefile 中必须使用 tab 而不是空格

  - `cp template/makefile.tmpl <your_path>/Makefile`

## 代码

### 如何增加新的模板以及生成脚本

- 在 template/ 中创建一个新的文件 <foo>.tmpl

- 在 gen.CmdType 中新增一个常量, 以及 CmdType.Vars 设置模板中对应的变量名

- 在 gen 中写一个 sub parser

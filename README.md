## 说明

生成一些常见的配置文件

## 目录结构

- `/template` 一些配置文件的模板, `{}` 中是一些生成配置文件时的变量

- `/conf` 最终配置文件生成的位置

- `gen_conf.py` 将模板转为配置文件的脚本

## 具体配置文件说明 & 应用

### flaskenv.tmpl

  - 生成配置文件 `python3 gen_conf.py flaskenv --app <app> --port <port>`

  - copy 复制文件 `cp conf/flaskenv.conf <your_path>/.flaskenv`

### git.tmpl

  - 生成配置文件 `python3 gen_conf.py git --name <name> --email <email>`

  - link 配置文件 `ln -s conf/git.conf ~/.gitconfig`

### gitignore.tmpl

  - `cp template/gitignore.tmpl <your_path>/.gitignore`

### makefile.tmpl

注意 Makefile 中必须使用 tab 而不是空格

  - `cp template/makefile.tmpl <your_path>/Makefile`

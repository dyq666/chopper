## 说明

生成一些常见的配置文件

## 目录结构

- `/template` 一些配置文件的模板 `{}` 中是一些动态改变的变量

- `/conf` 最终配置文件生成的位置

- `gen_conf.py` 通过 Python 脚本将模板变为配置文件

## 具体配置文件说明 & 应用

### flaskenv.conf

`cp conf/flaskenv.conf <your_path>/.flaskenv`

### git.conf

  - 一些命令的缩小 & 一些注释
 
  - 生成配置文件 `python3 gen_conf.py git --name <name> --email <email>`

  - 复制一份配置文件 `ln -s conf/git.conf ~/.gitconfig`

### gitignore.conf

`cp template/gitignore.conf <your_path>/.gitignore`

### makefile.conf

`cp template/makefile.conf <your_path>/Makefile`


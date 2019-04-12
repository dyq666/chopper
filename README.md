## 说明

生成一些常见的配置文件

## 目录结构

- `/template` 一些配置文件的模板 `{}` 中是一些动态改变的变量

- `/conf` 最终配置文件生成的位置

- `gen_conf.py` 通过 Python 脚本将模板变为配置文件


## 具体配置文件说明 & 应用

### 1. git
  - 一些命令的缩小 & 一些注释
  - 生成配置文件 `python3 gen_conf.py git -n <name> -e <email>`
  - 复制一份配置文件 `cp conf/git.conf ~/.gitconfig`

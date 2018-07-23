#!/usr/bin/env bash

# 安装 expect
command -v expect > /dev/null 2>&1
if [ "$?" != "0" ] ; then
    echo -e "当前机器尚未安装 expect。"
    echo -e "使用 yum 安装 except..."
    yum install -y expect 
fi

if [ $(command -v expect) ] ; then
    # 生成 ssh key
    chmod +x ssh-keygen.exp 
    ./ssh-keygen.exp > /dev/null 2>&1
    if [ "$?" == "0" ] ; then
   	    echo "生成公钥成功。"
    fi

    # 复制 ssh key 到各机器
    cat hosts | while read line
    do
        echo -e "${line}" > ./host.tmp
        #组织数组，读取各变量
 	    #xdhuxc=$(cat ./host.tmp)
	    #array=(${xdhuxc//\ / })
        #echo -e "target_host: ${array[0]}, username: ${array[1]}, password: ${array[2]}, port: ${array[3]}"
        #echo -e "--------------------------"
        cat host.tmp | awk -F '[: ]' '{print $1, $2, $3, $4}' | while read target_host username password port
	    do
            #echo -e "target_host: ${target_host}, username: ${username}, password: ${password}, port: ${port}"
		    if [ -z "${port}" ] ; then
			    port=22
		    fi
		    #current_user=$(whoami)
 		    file_path=/$(whoami)/.ssh/id_rsa.pub
        	if [ -n ${target_host} -a -n ${username} -a -n ${password} ] ; then
                ./ssh-copy-id.exp ${target_host} ${username} ${password} ${file_path} ${port} > /dev/null 2>&1
                if [ "$?" == "0" ] ; then
                    # 将该机器信息写入临时文件中，安装完ansible后，添加主机组
                    echo "机器 ${target_host} 添加公钥成功。"
                else
                    echo "机器 ${target_host} 添加公钥失败。"
                fi
        	fi
	    done
    done
fi 

# 安装 ansible
command -v ansible > /dev/null 2>&1
if [ "$?" != "0" ] ; then
    echo -e "当前机器尚未安装 ansible。"
    echo -e "使用 yum 安装 ansible..."
    yum install -y ansible
fi

# 删除临时文件 host.tmp
if [ -f ./host.tmp ] ; then
    rm -f ./host.tmp
fi

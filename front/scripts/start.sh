#!/bin/bash
set 'echo -e -o pipefail'

unix_today=$(date +'%s')
unix_today=$((unix_today+32400))
jst_ymd_today=$(date '+%Y/%m/%d %H:%M:%S' --date "@$unix_today")
app_name='app'

# プロジェクトディレクトリが存在していればサーバー起動
if [ -d /code/${app_name} ]; then
    # vueプロジェクト設定済みではなかったら
    if [ ! -f /code/${app_name}/vue.config.js ]; then
        echo "${jst_ymd_today} | Vue directory set up"
        # vueテンプレート作成
        bash /code/scripts/vue-settings.sh
        # axiosインストール
        npm install axios vue-router

        echo "----- Restart the container with the 'docker-compose up' command again -----"
    else
        echo "${jst_ymd_today} | Start the project server"
        # プロジェクトディレクトリに移動してサーバー起動
        cd ${app_name}
        npm run serve
    fi
else
    echo "「${jst_ymd_today}」| Create a new project"
    mkdir /code/${app_name}

    echo "----- Run the command 'docker-compose run front vue create ${app_name} .' on the host machine -----"
fi
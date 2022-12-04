#!/bin/bash
set 'echo -e -o pipefail'

# ルートディレクトリ取得
ROOT_DIR=$(cd $(dirname $0)/..;pwd)
app_name='app'

#***********************************************************************
echo "----- Vue axios設定ファイル作成 -----"
#***********************************************************************
cat > ${ROOT_DIR}/${app_name}/vue.config.js << "EOF"
module.exports = {
    devServer: {
        proxy: {
            '^/api/': {
                target: 'http://localhost:8000',
                logLevel: 'debug',
                pathRewrite: { "^/api/": "/api/" }
            }
        }
    }
}
EOF

#************************************************************************************************
echo "----- 「HelloWorld.vue」修正 -----"
#************************************************************************************************

sed -i -e "s/<h1>{{ msg }}<\/h1>/<h1>{{ msg }}<\/h1>\n<h2>現在の時間：{{ result }}<\/h2>\n<button @click=\"getAPI()\">クリック！<\/button>/" ${ROOT_DIR}/${app_name}/src/components/HelloWorld.vue

sed -i -e "N;s/}\n<\/script>/, data () {\n    return {\n      result: 'No Result',\n      url: 'http:\/\/localhost:8000\/api\/'\n    }\n  },\n  methods: {\n    getAPI () {\n      this.\$axios.get(this.url).then(response => {\n        this.result = response.data.status\n      })\n    }\n  }\n}\n<\/script>/" ${ROOT_DIR}/${app_name}/src/components/HelloWorld.vue

#************************************************************************************************
echo "----- main.js修正 -----"
#************************************************************************************************
cat > ${ROOT_DIR}/${app_name}/src/main.js << "EOF"
import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from './router.js'

Vue.config.productionTip = false
Vue.prototype.$axios = axios

new Vue({
    router,
    render: h => h(App),

}).$mount('#app')
EOF

#**********************************************************
echo "----- コンテンツテンプレート作成 -----"
#**********************************************************
cat > ${ROOT_DIR}/${app_name}/src/router.js << "EOF"
import Vue from 'vue'
import Router from 'vue-router'
import top from '@/components/top'
import page2 from '@/components/page2'
import page3 from '@/components/page3'


Vue.use(Router)
export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: top
        },
        {
            path: '/page2',
            component: page2
        },
        {
            path: '/page3',
            component: page3
        }
    ]
})
EOF

cat > ${ROOT_DIR}/${app_name}/src/components/top.vue << "EOF"
<template>
    <div>
        <p>ここはトップページです。</p>
        <h2>現在の日本時間：{{ result }}</h2>
        <button @click="getAPI()">クリック！</button>
    </div>
</template>

<script>
export default {
    name: 'jp-time',
    props: {
        msg: String
    },
    data () {
        return {
        result: '不明',
        url: 'http://localhost:8000/api/jp'
        }
    },
    methods: {
        getAPI () {
            this.$axios.get(this.url).then(response => {
                this.result = response.data.status
            })
        }
    }
}
</script>
<style>
</style>
EOF

cat > ${ROOT_DIR}/${app_name}/src/components/page2.vue << "EOF"
<template>
    <div>
        <p>ここは２ページ目です。</p>
        <h2>現在のアメリカ時間：{{ result }}</h2>
        <button @click="getAPI()">クリック！</button>
    </div>
</template>

<script>
export default {
    name: 'us-time',
    props: {
        msg: String
    },
    data () {
        return {
        result: '不明',
        url: 'http://localhost:8000/api/us'
        }
    },
    methods: {
        getAPI () {
            this.$axios.get(this.url).then(response => {
                this.result = response.data.status
            })
        }
    }
}
</script>
EOF

cat > ${ROOT_DIR}/${app_name}/src/components/page3.vue << "EOF"
<template>
    <div>
        <p>ここは３ページ目です。</p>
        <h2>現在のブラジル時間：{{ result }}</h2>
        <button @click="getAPI()">クリック！</button>
    </div>
</template>

<script>
export default {
    name: 'br-time',
    props: {
        msg: String
    },
    data () {
        return {
        result: '不明',
        url: 'http://localhost:8000/api/br'
        }
    },
    methods: {
        getAPI () {
            this.$axios.get(this.url).then(response => {
                this.result = response.data.status
            })
        }
    }
}
</script>
EOF

#*********************************************************
# "----- 「App.vue」修正 -----"
#*********************************************************

cat <<EOF > ${ROOT_DIR}/${app_name}/src/App.vue
<template>
    <div id="app">
        <div id="header">
            <!--リンクタグを生成します。-->
            <router-link to="/">top</router-link>41
            <router-link to="/page2">2</router-link>
            <router-link to="/page3">3</router-link>
        </div>
        <router-view></router-view>
    </div>
</template>

<!--コンポーネントの名前を定義します。-->
<script>
export default {
    name: 'App'
}
</script>

<!--スタイルの指定をします-->
<style>
body {
    margin: 0;
}

#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}
#header {
    height: 40px;
    background: white;
    box-shadow: 0px 3px 3px rgba(0,0,0,0.1);
    display: flex;
    justify-content: center;
    align-items: center;
}

#header a {
    text-decoration: none;
    color: #2c3e50;
    margin: 0 10px;
    padding: 3px 10px;
    background: #5ccebf;
}
</style>
EOF
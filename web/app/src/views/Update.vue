<template>
  <div class="flex">
    <div class="fixedGlobal">
      <GlobalHeader />
    </div>
    <div class="preOWrap flex">
      <div id="app">
        <div class="myIcon relative">
          <div v-if="image.length">
            <img :src="image" />
          </div>
          <div v-else>
            <img :src="data.icon_uri" alt="アイコン" v-cloak />
          </div>
          <label class="iconInput">
          <input type="file" @change="onFileChange">アイコン変更
          </label>
        </div>
      </div>
      <div>
        <p>ユーザー名</p>
        <input v-model="username" type="text" class="text" :placeholder="data.username" maxlength="40"/>
        <br />
        <p>タグ</p>
        <input v-model="tag" type="text" class="text"  :placeholder="data.tag" />
        <br />
        <div class="buttonWrap">
          <div class="signin">
            <router-link to="/myPage"><button>戻る</button></router-link>
          </div>
          <div class="button">
            <button @click="Submit()">更新</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { API_SERVER, IMG_URL } from "@/assets/config.js";
import GlobalHeader from "@/components/GlobalHeader.vue";
export default {
  name: "ImageView",
  data() {
    return {
      image: '',
      imgName: '',
      uploadFile: '',
      data: [],
      username: "",
      tag: "",
    };
  },
  components: {
    GlobalHeader,
  },
  methods: {
    onFileChange: function(e){
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
          return;
      }
      if (!files[0].type.match('image.*')) {
          return;
      }
      this.createImage(files[0]);
      this.uploadFile = files[0];
    },
    createImage(file) {
      // var image = new Image();
      var reader = new FileReader();
      var vm = this;
      reader.onload = function(e) {
          vm.image = e.target.result;
      };
      reader.readAsDataURL(file);
      vm.imgName = file.name;
    },
    Submit: function(e) {
      const token = this.$cookies.get("access");
      var formData = new FormData();
      var config = {
        headers: {
          'Authorization': "JWT " + token,
        }
      };
      
      if (this.uploadFile.length) {
        // formData.append("number", "123456");
        formData.append('icon_uri', this.uploadFile);
        var config = {
          headers: {
            'Authorization': "JWT " + token,
            'content-type': 'multipart/form-data',
          }
        }
        const requestBody = {
          username: this.username,
          tag: this.tag,
        };
        axios
          .patch(API_SERVER + "/api/v1/auth/users/me/",requestBody, formData, config)
          .then((response) => {
              console.log(response);
              this.$router.push("/myPage");
          })
          .catch((error) => {
              // error 処理
          })  
      }else{
        const requestBody = {
          username: this.username,
          tag: this.tag,
        };
        axios
          .patch(API_SERVER + "/api/v1/auth/users/me/",requestBody,{
            headers: { Authorization: "JWT " + token },
          })
          .then((response) => {
              console.log(response);
              this.$router.push("/myPage");
          })
          .catch((error) => {
              // error 処理
          })  
      }


    },
    Created: async function () {
      const token = this.$cookies.get("access");
      await axios
        .get(API_SERVER + "/api/v1/auth/users/me/", {
          headers: { Authorization: "JWT " + token },
        })
        .then((response) => {
          this.data = response.data;
          this.username = response.data.username;
          this.tag = response.data.tag;
          console.log(this.user);
          return;
        })
        .catch((e) => {
          console.log(e);
          return;
        });
    },
  },
  created() {
    if (this.$cookies.get("access") === null) {
      const refresh = this.$cookies.get("refresh");
      if (refresh != null) {
        console.log("リフレッシュ");
        const requestBody = {
          refresh: refresh,
        };
        axios
          .post(API_SERVER + "/api/v1/auth/jwt/refresh/", requestBody)
          .then((response) => {
            let token = response.data.access;
            this.$cookies.set("access", token, 60 * 30);
            location.reload();
          })
          .catch(() => {
            //エラー回避用
            this.$router.push("/SignIn");
          });
      }else{
        this.$router.push("/SignIn");
      }
      return;
    }
    this.Created();
  },
};
</script>

<style scoped>
.preOWrap {
  margin: 0 auto;
  padding-top: 100px;
  width: 800px;
  justify-content: space-between;
  z-index: 1;
}

.myIcon {
  width: 180px;
  height: 180px;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0px 0px 4px 1px rgb(80, 80, 80);
  
  display: flex;
  justify-content: center;
  align-items: center;

}
.myIcon div img {
  width: 180px;
  height: 180px;
  object-fit: cover;
}
p {
  font-size: 26px;
  font-weight: bold;
}
.text {
  width: 420px;
  height: 40px;
  background: #fff;
  /* border: solid 2px #ccc6c6; */
  margin: 4px 0 20px;
  padding: 6px 0 6px 10px;
  border-radius: 10px;
  box-shadow: 0px 0px 2px 2px #ccc inset;
}
.text:focus {
  outline: none;
}
.buttonWrap {
  margin-top: 100px;
  display: flex;
  justify-content: space-between;
}
button {
  color: #fff;
  background: #1e4fff;
  width: 140px;
  height: 54px;
  text-align: center;
  border-radius: 5px;
  margin-top: 20px;
  box-shadow: 1px 2px 1px 1px rgb(194, 194, 194);
}
button:hover {
  background: #0015ff;
}
label {
  display: none;
}
.myIcon:hover label {
  display: block;
  width: 180px;
  height: 180px;
  border-radius: 50%;
  overflow: hidden;
  position: absolute;
  top: 0;
  left: 0;
  background-color: rgba(255, 255, 255, 0.6);
  cursor: pointer;
  text-align: center;
  line-height: 180px;
  font-weight: bold;
}

input[type="file"] {
  display: none;
}
</style>

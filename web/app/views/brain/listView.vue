<template>
  <div class="wrapper" v-if="!Flags.ShareMode&&!this.$store.getters.getShareConfirmMode">
    <div class="my-pof">
      <img :src="UserStatus.icon_uri" alt="" class="prof-img">
      <div class="name-friend">
        <h1 class="my-name">{{ UserStatus.username }}</h1>
        <font-awesome-icon icon="fa-solid fa-gear" class="black-gear" inverse/>
      </div>
      <!--      <p class="m-id">{{ dummyUserStatus.userId }}</p>-->
      <p>
        <span class="m-tag" v-for="(tag,index) in UserStatus.userTag" :key="index">#{{ tag }}</span>
      </p>
    </div>
    <div class="my-list">
      <h1 class="list-h1">すべての記憶</h1>
      <button class="img-select" @click="toggleSelectMode">共有したい記憶を選択
        <font-awesome-icon icon="fa-regular fa-share" inverse/>
      </button>
      <div class="img-wrapper">
        <BrainStatusBox v-for="brains of BrainArray" :user-id="UserStatus.id" :note-id="brains.id" :image-URL="brains.image_uri"/>

      </div>
    </div>
    <div class="select-menu" v-if="this.$store.getters.getSelectMode">
      <button @click="closeSelectMode" class="back-button">戻る</button>
      <button class="go-select-button" @click="shareConfirm">選択画面へ</button>
    </div>
  </div>
  <div v-if="Flags.ShareMode&&!this.$store.getters.getShareConfirmMode">
    <ShareSelect :SelectBrains="SelectBrains"/>
  </div>

  <div id="share-confirm" v-if="this.$store.getters.getShareConfirmMode">
    <ShareConfirmMenu :SelectBrains="SelectBrains" @init="init"/>
  </div>

</template>

<script lang="ts">
import {defineComponent} from "vue"
import BrainStatusBox from "../../component/brain/BrainStatusBox.vue";
import ShareSelect from "../../component/brain/ShareSelectMenu.vue"
import ShareConfirmMenu from "../../component/brain/ShareConfirmMenu.vue";
import {getAuthHeader} from "../../lib/auth";
import {getUserBrain, getUserData} from "../../dummy/brain";
import {callAPI} from "../../lib/AxiosAccess";

export default defineComponent({
  components: {ShareConfirmMenu, BrainStatusBox, ShareSelect},
  data() {
    return {
      Flags: {
        ShareMode: false
      },
      UserStatus: {
        icon_uri:"",
        username:"memo:Re",
        user_tag:["HAL TOKYO","学生"]
      },
      BrainArray: [

      ],
      SelectBrains: []
    }
  },
  watch: {
    $route(to) {
      console.log(to)
      if (to.fullPath != "/mypage") {
        this.getFriendNote()
      } else {
        this.getMyNote()
      }

    }
  },
  beforeMount() {
    const routePath = this.$route
    console.log(routePath.fullPath)
    if (routePath.fullPath != "/mypage") {
      this.getFriendNote()
    } else {
      this.getMyNote()
    }
  },
  mounted() {
    this.$store.dispatch("resetSelectBrain")
    this.$store.dispatch("initShareFlags")

  },
  methods: {
    getMyNote:async function() {
      //      const userId =
      // this.dummyUserStatus = getUserData(this.$store.getters.getUserId)
      // this.BrainArray = getUserBrain(this.$store.getters.getUserId)

      const getMyDataResponse = await callAPI("auth/users/me/","GET", true)
      this.UserStatus = getMyDataResponse.data

      const getMyBrainResponse = await callAPI("brains/"+this.$store.getters.getUserId,"GET",true)
      this.BrainArray = getMyBrainResponse.data
    },
    getFriendNote() {
      this.$store.dispatch("offFriendModalState")
      const friendId = this.$route.params.UserId
      // FriendId取得完了
      console.log(friendId)

      const URL = "/brains/" + friendId

      this.dummyUserStatus = getUserData(parseInt(friendId))
      this.BrainArray = getUserBrain(parseInt(friendId))

    },
    toggleSelectMode() {
      this.$store.dispatch("toggleSelectMode")
    },
    closeSelectMode() {
      this.$store.dispatch("offSelectMode")
    },
    shareConfirm() {
      //
      const SelectBrains = []
      const selectedBrainId = this.$store.getters.getSelectBrain
      for (const Brain of getUserBrain(this.$store.getters.getUserId)) {
        console.log(selectedBrainId.indexOf(Brain.brainId))
        if (selectedBrainId.indexOf(Brain.noteId) != -1) {
          SelectBrains.push(Brain)
        }
      }
      console.log(SelectBrains)
      this.SelectBrains = SelectBrains
      this.Flags.ShareMode = true
    },
    init() {
      this.Flags.ShareMode = false
      this.SelectBrains = []
      this.$store.dispatch("initShareFlags")
    }
  }
})
</script>

<style scoped>
* {
  font-size: 10px
}

.wrapper {
  margin-top: 50px;
  margin-left: 50px;
  margin-right: 50px;
}

.prof-img {
  width: 100px;
  height: 100px;
  border: solid 1px;
  border-radius: 100%;
  margin-right: 20px;
  float: left;
}

.name-friend {
  display: flex;
  align-items: center;
}

.my-name {
  font-size: 3.2em;
}

.black-gear {
  color: black;
  width: 28px;
  height: 28px;
  margin-left: 20px;
}

.m-id {
  font-size: 1.8em;
}

.m-tag {
  font-size: 1.4em;
}

.my-list {
  margin-top: 70px;
  clear: both;
  position: relative;
}

.list-h1 {
  font-size: 22px;
  float: left;
  margin-bottom: 50px;
}

.img-select {
  font-size: 1.6em;
  color: #ffffff;
  background-color: #3D5093;
  width: 222px;
  height: 42px;
  border-radius: 10px;
  position: absolute;
  right: 0;
}

.img-wrapper {
  clear: both;
  display: flex;
  flex-wrap: wrap;
  gap: 50px;
}


.select-menu {
  position: fixed;
  width: 100%;
  height: 250px;
  left: 12%;
  padding-right: 12%;
  /*無理やりサイドメニュー分の長さのPaddingを追加して要素自体ではなく画面全体から見て中央に配置出来るようにする*/
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.back-button {
  width: 150px;
  height: 50px;
  background: #3D5093;
  margin: 15px;
  font-size: 18px;
  color: #ffffff;
  border-radius: 10px;
}

.go-select-button {
  width: 150px;
  height: 50px;
  background: #BE3455;
  margin: 15px;
  font-size: 18px;
  color: #ffffff;
  border-radius: 10px;
}

</style>

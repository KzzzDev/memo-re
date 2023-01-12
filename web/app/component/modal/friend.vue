<template>
  <div class="flex flex-row w-full h-screen text-neutral-600">
    <div class="w-60 h-screen bg-stone-200">
      <ul class="py-8">
        <li>
          <a class="flex flex-row pl-8" href="">
            <img class="w-12 h-12 rounded-full object-cover mr-3 bg-white" :src="myStatus.icon_uri">
            <div>
              <h1 class="text-xl font-semibold">{{ myStatus.name }}</h1>
            </div>
          </a>
        </li>
      </ul>
      <h1 class="text-xs pl-2 pb-2 font-semibold">フレンドリスト</h1>
      <ul>
        <li v-for="friend of friendList">
          <router-link class="flex flex-row pl-8 py-2 border-y border-neutral-300" :to="/brain/+friend.userId">
            <img class="w-10 h-10 rounded-full object-cover mr-3 bg-white" :src="friend.icon">
            <div>
              <h1 class="font-semibold">{{ friend.name }}</h1>
            </div>
          </router-link>
        </li>
      </ul>
    </div>
    <div class="flex items-center justify-center w-6 h-20 mt-20 bg-stone-200 rounded-tr-lg rounded-br-lg">
      <font-awesome-icon icon="fa-solid fa-user-group"/>
    </div>
  </div>
</template>

<script lang="js">
import {getFriendList, getUserData} from "../../dummy/brain";
import {callAPI} from "../../lib/AxiosAccess";

export default {
  name: "friend-modal",
  data() {
    return {
      myStatus: {},
      friendList: []
    }
  },
  beforeMount() {
  },
  methods: {
    initData: async function () {
      const getMyDataResponse = await callAPI("auth/users/me/", "GET", true)
      this.myStatus = getMyDataResponse.data
      // 出来次第FriendAPI処理実装
      const getFriendDataResponse = ""
      this.friendList = getFriendList(this.$store.getters.getUserId)

    }
  }
}
</script>

<style scoped>

</style>
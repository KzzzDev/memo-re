<template>
  <div class="status-wrapper">
    <div class="status-info mt-24">
      <StatusMain :noteStatus="dummyNoteStatus" @request="sendRequest" />

    </div>
    <div class="status-list mt-16 py-2 w-10/12 mx-auto flex gap-6 ">
      <router-link v-for="note in dummyOtherNoteList" :to="'/note/'+note.noteId" :key="note.noteId">
        <img :src="note.image_uri" alt="" class="w-28 h-28 shadow-lg">
      </router-link>
    </div>
  </div>
  <div id="request-modal" class="w-full h-full fixed top-0 left-0 flex justify-center items-center" v-show="ShowRequestModal" @click.self="ShowRequestModal=false">
    <div class="modal-wrap w-6/12 py-16 border-solid bg-white border-2 shadow-md rounded-xl">
      <h1 class="text-4xl text-center mb-12" v-show="!Finished">共有申請しますか？</h1>
      <h1 class="text-4xl text-center mb-12" v-show="Finished">申請されました！</h1>
      <div class="wrapper w-full">
        <img :src="userData.icon_uri" alt="" class="w-28 h-28 shadow-lg rounded-full mx-auto">
        <p class="user-name text-center my-4">{{ userData.name }}</p>
        <div class="img-wrap flex justify-center gap-4">
           <img :src="dummyNoteStatus.image_uri" alt="" class="w-24 h-24 shadow-lg" draggable="false">
        </div>
      </div>
      <div class="button flex justify-center gap-6 mt-12" v-show="!Finished">
        <button class="w-32 bg-gray-400 text-white py-3 rounded-md" @click="ShowRequestModal=false">キャンセル</button>
        <button class="w-32 bg-red-700 text-white py-3 rounded-md" @click="Finished=true">申請</button>
      </div>
      <div class="button flex justify-center gap-6 mt-12" v-show="Finished">
        <button class="w-32 bg-blue-700 text-white py-3 rounded-md" @click="ShowRequestModal=false">
          完了
        </button>
      </div>

    </div>
  </div>
</template>

<script>
import StatusMain from '../../component/brain/statusMain.vue';
import {getNoteStatus, getUserBrain, getUserData} from "../../dummy/brain";
import {callAPI} from "../../lib/AxiosAccess";

export default {
  name: 'status',
  data() {
    return {
      dummyNoteStatus: {},
      dummyOtherNoteList: [],
      ShowRequestModal:false,
      Finished:false,
      userData:{

      }
    }
  },
  components: {
    StatusMain
  },
  watch: {
    $route(to) {
      this.getNoteData()
    }
  },
  beforeMount() {
    const noteId = this.$route.params.NoteId
    console.log(noteId)
    this.dummyNoteStatus = getNoteStatus(parseInt(noteId))
    if (!this.dummyNoteStatus){
      this.$router.push("/error")
    }
    callAPI("auth/users/me/","GET", true).then(
        getMyDataResponse=>{
          this.userData =  getMyDataResponse.data


        }
    )



  },
  methods:{
    sendRequest(){
      this.ShowRequestModal = true
    },
    getNoteData:async function(){
      const noteId = this.$route.params.NoteId
      const endPoint =`brains/${this.$store.getters.getUserId}/${noteId}`
      const getNoteDataResponse = await callAPI(endPoint,"GET", true)
    }
  }
};
</script>

<style scoped>
.status-list {
  overflow-x: scroll;
}

.status-list img {
  flex-shrink: 0;
}
</style>

<template>
  <div v-if="!Flags.Preview">
    <div class="w-full flex justify-center">
      <section class="flex w-1/2 mt-16 border border-black flex-col p-5">
        <div>
          <label for="note-title" class="block text-gray-900">題名</label>
          <input v-model="Forms.Title" type="text" id="note-title"
                 class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                 required>
        </div>
        <div>
          <label for="note-keyword" class="block text-gray-900">キーワード</label>
          <input v-model="Forms.Keyword" type="text" id="note-keyword"
                 class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                 required>
        </div>
        <div>
          <label for="note-memo" class="block text-gray-900">説明</label>
          <textarea v-model="Forms.Memo" type="text" id="note-memo"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                    required></textarea>
        </div>
        <div class="w-full flex justify-end mt-10">
          <button class="bg-blue-500 hover:bg-blue-400 text-white rounded px-4 py-2 shadow" @click="callCreateImageAPI">
            画像を作成
          </button>
        </div>
      </section>

    </div>
    <section v-if="Flags.Creating||Flags.Finished" id="creating" class="flex justify-center align-center fixed">
      <div v-if="Flags.Creating" class="w-80 h-64 border border-black bg-white flex align- flex-col p-5 justify-around">
        <font-awesome-icon icon="fa-solid fa-spinner" size="6x" spin/>
        <p>生成中(20~30秒ほどかかります。リロードすると生成できないので気を付けてください)</p>
      </div>
      <div v-else-if="Flags.Finished"
           class="w-80 h-64 border border-black bg-white flex align- flex-col p-5 justify-around">
        <font-awesome-icon icon="fa-regular fa-circle-check" size="6x"/>
        <p>生成されました！</p>
        <button class="bg-blue-500 hover:bg-blue-400 text-white rounded px-4 py-2 shadow" @click="Flags.Preview = true">
          確認する。
        </button>

      </div>
    </section>
  </div>
  <!-- プレビュー画面に切り替え /-->
  <div v-if="Flags.Preview">
    <div class="flex flex-col justify-center w-full ">
      <status-main :note-status="NoteStatus" :preview-mode="true"/>
      <div class="w-full flex justify-center mt-5">
        <button class="bg-white hover:bg-gray-100 text-gray-800  rounded px-8 py-4 m-5 shadow"
                @click="location.reload()">やり直す
        </button>
        <button class="bg-blue-500 hover:bg-blue-400 text-white rounded px-8 py-4 m-5 shadow"
                @click="callCreateNoteAPI">作成
        </button>
      </div>
    </div>
    <div v-show="Flags.Created" class="w-full h-full fixed top-0 left-0 justify-center items-center">
      <div class="w-1/2 h-36 flex border shadow bg-white">
        <p>作成されました！</p>
        <button class="bg-blue-500 hover:bg-blue-400 text-white rounded px-8 py-4 m-5 shadow">
          <router-link to="/mypage">一覧に戻る。</router-link>
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent} from "vue"
import {createNote} from "../../lib/network";
import statusMain from "../../component/brain/statusMain.vue"
import axios from "axios";
import {getNextId, insertNoteData} from "../../dummy/brain";
import {callAPI} from "../../lib/AxiosAccess";

type Flags = {
  Creating: boolean,
  Finished: boolean,
  Preview: boolean,
  Created: boolean
}

type Forms = {
  Title: string,
  Keyword: string,
  Memo: string
}


export default defineComponent({
  data() {
    return {
      Flags: {
        Creating: false,
        Finished: false,
        Preview: false,
        Created: false
      } as Flags,
      Forms: {
        Title: "",
        Keyword: "",
        Memo: ""
      } as Forms,
      NoteStatus: {}
    }

  },
  components: {
    statusMain
  },
  methods: {
    callCreateImageAPI: async function () {
      //
      this.Flags.Creating = true
      // Create Image
      const postParams = new URLSearchParams()
      postParams.append("keyword", this.Forms.Keyword)
      postParams.append("user_id", "test")
      try {
        const formatKeyword = this.Forms.Keyword.replaceAll(" ", ",").replaceAll("　", ",")

        const CreateAiImageResponse = await axios.post("http://20.66.79.230:8080/ai/debug/", {
          keyword: formatKeyword,
          user_id: this.$store.getters.getUserId
        })
        console.log(CreateAiImageResponse)
        const image_uri = "http://20.78.36.224/images/" + CreateAiImageResponse.data.img_file
        this.NoteStatus = {
          title: this.Forms.Title,
          keyword: formatKeyword,
          text_uri: this.Forms.Memo,
          image_uri: image_uri,
          userId: this.$store.getters.getUserId,
          ownerId: this.$store.getters.getUserId,
          noteId: getNextId()
        }
        const CreateNoteRequest =
            {
              "user": this.$store.getters.getUserId,
              "title": this.Forms.Title,
              "keyword": formatKeyword,
              "image_uri": image_uri,
              "text_uri": this.Forms.Memo,
              "is_public": true
            }

        const CreateNoteResponse = await callAPI("brains/"+this.$store.getters.getUserId,"POST",true,CreateNoteRequest)
        console.log(CreateNoteResponse)
      } catch (e) {
        console.log(e)
      } finally {

        this.Flags.Creating = false
        this.Flags.Finished = true
      }


      // noteの画像データ取得


    },
    callCreateNoteAPI: async function () {

      insertNoteData(this.NoteStatus)
      this.Flags.Created = true

    }
  }
})


</script>

<style scoped>
#creating {
  top: 0;
  left: 12%;
  display: flex;
  justify-content: center;
  width: 88%;
  height: 100%;
  align-items: center;
}


#note-memo {
  height: 180px;
  resize: none;
}
</style>

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
          <button class="bg-blue-500 hover:bg-blue-400 text-white rounded px-4 py-2" @click="callCreateImageAPI">画像を作成</button>
        </div>
      </section>

    </div>
    <section v-if="Flags.Creating||Flags.Finished" id="creating" class="flex justify-center align-center fixed">
      <div v-if="Flags.Creating" class="w-80 h-64 border border-black bg-white flex justify-center">
        <font-awesome-icon icon="fa-solid fa-spinner" size="lg" spin/>
        <p>生成中</p>
      </div>
      <div v-else-if="Flags.Finished" class="w-80 h-64 border border-black bg-white flex justify-center">
        <font-awesome-icon icon="fa-solid fa-spinner" size="lg" spin/>
        <p>生成されました！</p>
      </div>
    </section>
  </div>
    <!-- プレビュー画面に切り替え /-->
  <div v-if="Flags.Preview">
    <div class="flex justify-center w-full ">
      <div class="w-full ">
        <button>やり直す</button>
        <button @click="callCreateNoteAPI">作成</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent} from "vue"
import {createNote} from "../../lib/network";


type Flags = {
  Creating: boolean,
  Finished: boolean,
  Preview: boolean
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
        Preview: false
      } as Flags,
      Forms: {
        Title: "",
        Keyword: "",
        Memo: ""
      } as Forms
    }

  },
  methods: {
    callCreateImageAPI: async function () {
      //
      this.Flags.Creating = true
      // Create Image
      await setTimeout(() => {
        this.Flags.Creating = false
      }, 10000)
      this.Flags.Creating = false
      this.Flags.Finished = true

      // noteの画像データ取得


    },
    callCreateNoteAPI:async function(){


     const fetchResult =  await createNote({
        title:this.Forms.Title,

      })

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

</style>

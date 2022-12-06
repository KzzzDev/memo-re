<template>
  <div class="form-wrapper">
    <div class="image-generate-preview">
      <img src="" alt="">
    </div>

    <div class="memory-info-input">
      <dl>
        <dd>
          <input type="text" placeholder="タイトル" v-model="titleInput">
        </dd>
        <dd>
          <select v-model="eraSelect">
            <option selected disabled>年代</option>
            <option value="">小学校</option>
          </select>
        </dd>
        <dd>
          <textarea v-model="memoTextarea"></textarea>
        </dd>
        <dd>
          <button @click="">作成！</button>
        </dd>
      </dl>
    </div>

  </div>
</template>

<script setup lang="ts">

import {ref} from "vue";

// とりあえず各フォーム入力バインディング用変数は　目的+タグで表記
const titleInput = ref("")
const memoTextarea = ref("")
const eraSelect = ref(null)



</script>

<style scoped>
.form-wrapper {
  display: flex;
  justify-content: flex-start;
}

.image-generate-preview {
  width: 50%;
  box-sizing: border-box;
  border-right: solid 1px;
}

.memory-info-input {
  width: 50%;
  display: flex;
  flex-direction: column;
}

input,select,button{
  width: 480px;
  height: 40px;
  margin: 0 0 10px;
  padding: 0 5px;
  outline: 0;
  background: #fff;
  border: solid 1px #808080;
  box-sizing: border-box;
}

textarea{
  width: 480px;
  height: 200px;
  margin: 0 0 10px;
  padding: 0 5px;
  outline: 0;
  background: #fff;
  border: solid 1px #808080;
  box-sizing: border-box;
  resize: none;
}
</style>

<template>
  <div class="form-wrapper">
    <div class="image-generate-preview">
      <img src="" alt="">
    </div>

    <div class="memory-info-input">
      <dl>
        <dd>
          <input type="text" placeholder="タイトル" v-model="titleInput">
          <p v-show="!!titleError">{{ titleError }}</p>
        </dd>
        <dd>
          <select v-model="eraSelect">
            <option value="-1" selected disabled>年代</option>
            <option value="1">小学校</option>
          </select>
          <p v-show="!!eraError">{{ eraError }}</p>

        </dd>
        <dd>
          <textarea v-model="memoTextarea"></textarea>
          <p v-show="!!memoTextError">{{ memoTextError }}</p>
        </dd>
        <dd>
          <button @click="submit">作成！</button>
        </dd>
      </dl>
    </div>

  </div>
</template>

<script setup lang="ts">
import {computed, watch} from "vue";
import {useBackend, useError} from "../../lib";
import {createNote} from "../../lib/network";
import validator from "validator";

import {useRouter} from "vue-router";
const {push} = useRouter()

const {
  data: titleInput,
  error: titleError,
  start: tStart,
} = useError("", [validator.isEmpty], {
  defaultMessage: "タイトルを入力してください。",
  immediately: false,
});

const {
  data: memoTextarea,
  error: memoTextError,
  start: mStart,
} = useError("", [validator.isEmpty], {
  defaultMessage: "テキストを入力してください。",
  immediately: false
})

const {
  data: eraSelect,
  error: eraError,
  start: eStart,
} = useError(-1, [value => value < 0], {
  defaultMessage: "年代を選択してください。",
  immediately: false
})

const valid = computed(() => !(titleError.value || memoTextError.value || eraError.value));

const submit = () => {
  tStart();
  mStart();
  eStart();

  if (valid) {
    CreateNote()
  }
}

const {data, error, refresh: CreateNote} = useBackend(createNote, false, {
  title: titleInput,
  category: eraSelect,
  content: memoTextarea
});
watch(data, (value) => !!value && push({path: "/list"}));

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

input, select, button {
  width: 480px;
  height: 40px;
  margin: 0 0 10px;
  padding: 0 5px;
  outline: 0;
  background: #fff;
  border: solid 1px #808080;
  box-sizing: border-box;
}

textarea {
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

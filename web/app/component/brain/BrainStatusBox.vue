<template>
  <div class="img-box" v-if="$store.getters.getSelectMode">
    <div v-if="!this.isActive" class="shadow-filter"></div>

    <img :src="imageURL" alt="images" class="list-img">
    <input @change="change" v-model="isActive" :name="'cb-'+noteId" class="img-checkbox"
           type="checkbox" :id="'img-'+noteId"/>
    <label :for="'img-'+noteId"/>


  </div>
  <div class="img-box" v-else>
    <router-link :to="`/note/${userId}/${noteId}`">
      <img :src="imageURL" alt="images" class="list-img">
    </router-link>

  </div>
</template>

<script>
// TODO:inputとLabelの表示を切り替えると高さが変わるけどクリティカルではないので可能なときに直す
export default {
  name: "BrainStatusBox",
  data() {
    return {
      isActive: false
    }
  },
  props: {
    imageURL: {
      type: String,
      default: "../../public/images/brains/img001.png"
    },
    noteId: {
      type: Number,
      default: 0
    },
    userId: {
      type: Number,
      default: 0
    }
  },
  methods: {
    change: async function () {
      console.log(this.isActive)
      if (this.isActive) {
        await this.$store.dispatch("appendSelectBrain", this.noteId)
        return
      }
      await this.$store.dispatch("removeSelectBrain", this.noteId)
    }
  }

}
</script>

<style scoped>

.img-box {
  position: relative;
}

.list-img {
  width: 180px;
  height: 180px;
  box-shadow: black;
  border: solid 1px;
}

.img-checkbox {
  position: absolute;
  top: 12px;
  right: 12px;
}

input[type="checkbox"] {
  display: none;
}

input[type="checkbox"] + label {
  display: none;
  cursor: pointer;
  display: inline-block;
  position: relative;
  padding-left: 25px;
  padding-right: 10px;
}

input[type="checkbox"] + label::before {
  content: "";
  position: absolute;
  display: block;
  box-sizing: border-box;
  width: 24px;
  height: 24px;
  margin-top: -180px;
  margin-left: 146px;
  left: 0;
  border-radius: 50%;
  border: 2px solid;
  border-color: #585753; /* 枠の色変更 お好きな色を */
  background-color: #fff; /* 背景の色変更 お好きな色を */
}

input[type="checkbox"]:checked + label::after {
  content: "";
  position: absolute;
  display: block;
  box-sizing: border-box;
  width: 14px;
  height: 6px;
  margin-top: -172px;
  margin-left: 148px;
  left: 3px;
  transform: rotate(-45deg);
  border-bottom: 3px solid;
  border-left: 3px solid;
  border-color: #3C3C3C; /* チェックの色変更 お好きな色を */
}

.shadow-filter {
  position: absolute;
  width: 100%;
  height: 180px;
  background: #9ca3af;
  opacity: 0.5;
  top: 0;
  left: 0;
}

</style>
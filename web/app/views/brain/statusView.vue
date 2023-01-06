<template>
  <div class="status-wrapper">
    <div class="status-info mt-24">
      <StatusMain :noteStatus="dummyNoteStatus"/>
    </div>
    <div class="status-list mt-16 py-2 w-10/12 mx-auto flex gap-6">
      <router-link v-for="note in dummyOtherNoteList" :to="'/note/'+note.brainId" :key="note.brainId">
        <img :src="note.image_uri" alt="" class="w-28 h-28 shadow-lg">
      </router-link>
    </div>
  </div>
</template>

<script>
import StatusMain from '../../component/brain/statusMain.vue';
import {getNoteStatus, getUserBrain} from "../../dummy/brain";

export default {
  name: 'status',
  data() {
    return {
      dummyNoteStatus: {},
      dummyOtherNoteList: []
    }
  },
  components: {
    StatusMain
  },
  watch: {
    $route(to) {
      const noteId = to.params.NoteId
      console.log(noteId)
      this.dummyNoteStatus = getNoteStatus(parseInt(noteId))
    }
  },
  beforeMount() {
    const noteId = this.$route.params.NoteId
    console.log(noteId)
    this.dummyNoteStatus = getNoteStatus(parseInt(noteId))
    console.log(getUserBrain(this.dummyNoteStatus.userId))
    this.dummyOtherNoteList = getUserBrain(parseInt(this.dummyNoteStatus.userId))

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

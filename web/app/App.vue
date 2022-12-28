<template>
  <GlobalHeader />
  <main>
    <router-view @update:user-info="refreshUser" />
  </main>
</template>

<script lang="ts">
import { Ref } from "vue";
import { User, UserCredential } from "./lib/network";

/**
 * Key to inject user info into components.
 */
export const UserInfoKey = Symbol();
type _UserInfo = User & Pick<UserCredential, "email">;
/**
 * Type of user info to be injected.
 *
 * @see {@link UserInfoKey}
 */
export type UserInfo = Ref<_UserInfo>;
</script>

<script setup lang="ts">
import { provide, ref, watch } from "vue";

import { useBackend } from "./lib";
import { getUserInfo } from "./lib/network";

import GlobalHeader from "./component/GlobalHeader/Main.vue";

// #region Provide user info across the app
const { data: userRes, refresh: refreshUser } = useBackend(getUserInfo);
const userInfo = ref<_UserInfo>();
watch(userRes, (value) => (userInfo.value = value?.user));
provide(UserInfoKey, userInfo);
// #endregion
</script>

<style>
main {
  /*仮でヘッダーの大きさを12％に指定。*/
  width: 88%;
  margin-left: 12%;
}
</style>

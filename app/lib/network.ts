//#region Prelude
const baseUrl = process.env.API_SERVER;

interface Error {
  errors: [{ message: string }];
}

interface ResponseBase {
  status: number;
  error: Error;
}

export type APIResponse<T> = ResponseBase & T;

export type ErrorResponse = ResponseBase;

export const access = <T, U = {}>(
  endpoint: string,
  body?: U,
  options?: Partial<{
    method: "GET" | "POST" | "PUT" | "DELETE";
    headers: HeadersInit;
  }>,
  validator = (res: Response) => res.status == 200
) =>
  fetch(`${baseUrl}/${endpoint}`, {
    body: body && JSON.stringify(body),
    method: options?.method ?? "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer <Token>`, //! Utilize JWT token
      ...options?.headers,
    },
  }).then<APIResponse<T>>((res) => {
    return (validator(res) ? Promise.resolve : Promise.reject)(res.json());
  });
//#endregion

type NoteCategory = number;

type NoteId = string;

export interface NoteBrief {
  category: NoteCategory;
  title: string;
}

export interface NoteTemplate extends NoteBrief {
  content: string;
}

export interface Note extends NoteTemplate {
  imageUrl: string;
}

type UserId = string;

type UserName = string;

export interface UserCredential {
  email: string;
  password: string;
}

export interface User {
  id?: UserId;
  name: UserName;
  icon: string;
}

export interface FriendActionPayload {
  opponent: UserId;
}

export type NoteModificationPayload = NoteTemplate;

//#region User
export const registerUser = (info: UserCredential & { name: string }) => access(`users`, info, { method: "POST" });

export const getUserInfo = (userId: UserId) => access(`users/${userId}`);

export const updateUserInfo = (userId: UserId, info: User & UserCredential) =>
  access(`users/${userId}`, info, { method: "POST" });
// #endregion

//#region Friends
export const listFriends = () => access<{ friends: User[] }>(`friends`);

export const removeFriend = (payload: FriendActionPayload) => access(`friends`, payload, { method: "DELETE" });

export const applyFriendRequest = (payload: FriendActionPayload) =>
  access(`friends/request`, payload, { method: "POST" });

export const acceptFriendRequest = (payload: FriendActionPayload) =>
  access(`friends/request`, payload, { method: "POST" });

export const cancelFriendRequest = (payload: FriendActionPayload) =>
  access(`friends/request`, payload, { method: "DELETE" });
//#endregion

//#region Brain
export const listNotes = () => access<{ notes: NoteBrief[] }>(`brains`);

export const createNote = (payload: NoteModificationPayload) => access(`brains`, payload, { method: "POST" });

export const getNote = (noteId: NoteId) => access<{ note: Note }>(`brains/${noteId}`);

export const updateNote = (noteId: NoteId, payload: NoteModificationPayload) =>
  access<{ note: Note }>(`brains/${noteId}`, payload, { method: "PUT" });

export const deleteNote = (noteId: NoteId) =>
  access<{ note: Note }>(`brains/${noteId}`, undefined, { method: "DELETE" });

export const createNoteShare = (noteId: NoteId) => access(`brains/${noteId}/share`, undefined, { method: "POST" });

export const removeNoteShare = (noteId: NoteId) => access(`brains/${noteId}/share`, undefined, { method: "DELETE" });
//#endregion

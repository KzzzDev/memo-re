import axios from "axios";
import {getToken} from "./auth";

const serverAddress = "http://localhost:8000/api/v1"

type Method = "GET" | "POST" | "PUT" | "DELETE"

export const callAPI = async (endPoint: string, method: Method, useAuth: boolean, postData?: object) => {
    console.log("call API")
    const AxiosURL = `${serverAddress}/${endPoint}`
    const Header = useAuth ?
        {
            headers: {
                'accept': 'application/json',
                "Content-Type": "application/json",
                'X-CSRFTOKEN': "q8r8FyHxEWA0ZIiisnKkm5jKNRzUUF9yWYxYmNm5zgq3LrDC5NPMtIexOXvpMX8o",
                "Authorization": `JWT ${getToken()}`
            }
        }
        :
        {
            headers: {
                'accept': 'application/json',
                "Content-Type": "application/json",
                'X-CSRFTOKEN': "q8r8FyHxEWA0ZIiisnKkm5jKNRzUUF9yWYxYmNm5zgq3LrDC5NPMtIexOXvpMX8o",
            }
        }
    let response = ""
    console.log("switch前")
    switch (method) {
        case "GET":
            response = await axios.get(AxiosURL, Header)
            break;
        case "POST":
            console.log("Call Post")
            response = await axios.post(AxiosURL, postData, Header)
            break;
        case "DELETE":
            response = await axios.delete(AxiosURL, postData, Header)
            break;
        case "PUT":
            response = await axios.put(AxiosURL, postData, Header)
            break;
        default:
            console.log("xxxxxxxxxxxxxxx")
    }
    console.log("Call後")
    console.log(response)
    return response

}
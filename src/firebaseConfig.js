// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { initializeAppCheck, ReCaptchaV3Provider } from "firebase/app-check";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAspe6DOvtD2wE5NwjcTX_HxLe5e4Lbj7A",
  authDomain: "mysite-1383.firebaseapp.com",
  projectId: "mysite-1383",
  storageBucket: "mysite-1383.appspot.com",
  messagingSenderId: "461237373348",
  appId: "1:461237373348:web:86a668bddcfcaafca39931",
  measurementId: "G-Q46QVHN6E8",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

const appCheck = initializeAppCheck(app, {
  provider: new ReCaptchaV3Provider("6LcOyLQdAAAAAML71Vv35GBYNIoXtrQnAAQudkvK"),

  // Optional argument. If true, the SDK automatically refreshes App Check
  // tokens as needed.
  isTokenAutoRefreshEnabled: true,
});

export { analytics, appCheck };

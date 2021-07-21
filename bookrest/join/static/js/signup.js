const signupForm = document.querySelector(".signupForm");
const name = document.querySelector(".name");
const major = document.querySelector(".major");
const studentID = document.querySelector(".studentID");
const email = document.querySelector(".email");
const password = document.querySelector(".password");
const phoneNumber = document.querySelector(".phoneNumber");
const checkbox = document.querySelector(".checkbox");
const checkboxErrorMsg = document.querySelector(".js-checkboxErrorMsg");

const handleCheckboxForm = () => {
  console.log("혜성이뚱떙이");
  if (!checkbox.checked) {
    checkboxError(`이용규정에 동의해주세요`);
  } else {
    successCheckbox();
  }
};

const checkboxError = (message) => {
  checkboxErrorMsg.innerText = message;
};

const successCheckbox = () => {
  checkboxErrorMsg.innerText = "";
};

const errorRed = (input, message) => {
  const formControl = input.parentElement;
  formControl.classList.add("error");
  const small = formControl.querySelector("small");
  small.innerText = message;
};

const successLight = (input) => {
  const formControl = input.parentElement;
  formControl.classList.remove("error");
};

const setDefault = (input) => {
  const formControl = input.parentElement;
  formControl.className = "signupBoxTool__signupBox__form-control";
  //   const checkboxControl = check.parentElement;
  //   checkboxControl.className = "signupBoxTool__signupBox__rule";
};

const checkstudentID = () => {
  if (studentID.value.length === 9) {
    successLight(studentID);
  } else {
    errorRed(studentID, `학번을 정확히 입력해주세요`);
  }
};

const checkPassword = () => {
  if (password.value.length >= 6) {
    successLight(password);
  } else {
    errorRed(password, `비밀번호는 6자 이상이어야 합니다`);
  }
};

const checkEmail = () => {
  const emailRule =
    /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  if (emailRule.test(email.value.trim())) {
    successLight(email);
  } else {
    errorRed(email, `이메일이 유효하지 않습니다`);
  }
};

const loadName = () => {
  if (name.value.length === 0) {
    errorRed(name, `사용자 이름은 2자 이상이어야 합니다`);
  } else if (name.value.length >= 2) {
    successLight(name);
  } else {
    errorRed(name, `사용자 이름은 2자 이상이어야 합니다`);
  }
};

const signInit = () => {
  name.addEventListener("input", loadName);
  email.addEventListener("input", checkEmail);
  password.addEventListener("input", checkPassword);
  studentID.addEventListener("input", checkstudentID);
  checkbox.addEventListener("change", handleCheckboxForm);

  signupForm.addEventListener("submit", (e) => {
    e.preventDefault();
    checkPassword(password, 1, 6);
    loadName();
    checkEmail(email);
    checkstudentID(studentID);
    handleCheckboxForm();
  });
};

signInit();

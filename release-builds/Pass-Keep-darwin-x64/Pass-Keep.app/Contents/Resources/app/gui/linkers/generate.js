let { PythonShell } = require("python-shell");
var path = require("path");
var { dialog } = require("electron");

function generate_pass() {
  var app_name = document.getElementById("app-name").value;
  var pass_len = document.getElementById("pass-len").value;
  var with_special = document.getElementById("with-special").value;

  var options = {
    scriptPath: path.join(__dirname, "/../engine/"),
    args: [app_name, pass_len, with_special]
  };

  let pyshell = new PythonShell("generate_pass.py", options);

  pyshell.on("message", function(message) {
    console.log("message", message);
    // swal(
    //   "Thank You, your password has been created.\n" +
    //     "    Please look for pass-keep-public.txt on your Desktop"
    // );
  });
  document.getElementById("app-name").value = "";
  document.getElementById("pass-len").value = "";
  document.getElementById("with-special").value = "";
}

function generate_email() {
  var sender_email = document.getElementById("sender-email").value;
  var sender_password = document.getElementById("sender-password").value;

  console.log("email", sender_email);
  console.log("pass", sender_password);
  var options = {
    scriptPath: path.join(__dirname, "/../engine/"),
    args: [sender_email, sender_password]
  };

  let pyshell = new PythonShell("sending_email.py", options);

  const messageOptions = {
    type: "question",
    buttons: ["Done"],
    defaultId: 2,
    title: "Question",
    message: "Thank You | Pass Keep",
    detail: "Please check your email"
  };

  pyshell.on("message", function(message) {
    console.log("message", message);
    // dialog.showMessageBox(null, messageOptions, res => {
    //   console.log("res", res);
    // });
  });
  document.getElementById("sender-email").value = "";
  document.getElementById("sender-password").value = "";
}

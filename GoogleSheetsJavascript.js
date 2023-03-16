function GPT3(prompt) {
  var paramName = "input"
  var baseURL = "https://YOURREPL/gpt3"
  var encodedValue = encodeURIComponent(prompt);
  var url = baseURL + '?' + paramName + '=' + encodedValue;
  var response = UrlFetchApp.fetch(url);
  return response.getContentText();
}

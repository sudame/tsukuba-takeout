interface Window {
  onTokenCreated: Function;
}

window.onTokenCreated = (res: any) => {
  console.log(res);
};

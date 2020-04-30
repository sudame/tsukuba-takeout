import reactDOM from 'react-dom';
import React from 'react';
import StoreView from './_store';

const DOMContentLoadedHandler = () => {
  const appElement = document.getElementById('app')!;
  console.log(appElement);
  reactDOM.render(<StoreView />, appElement);
};

window.addEventListener('DOMContentLoaded', DOMContentLoadedHandler);

import reactDOM from 'react-dom';
import React from 'react';
import { Store } from './types';
import StoreListView from './components/_StoreListView';

declare var storeList: Store[];

const DOMContentLoadedHandler = () => {
  const appElement = document.getElementById('app')!;
  console.log(appElement);
  reactDOM.render(<StoreListView storeList={storeList} />, appElement);
};

window.addEventListener('DOMContentLoaded', DOMContentLoadedHandler);

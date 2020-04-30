import React from 'react';
import { Store } from '../types';
import StoreListViewItem from './_StoreListViewItem';

type StoreListViewProps = {
  storeList: Store[];
};

const StoreListView: React.FC<StoreListViewProps> = ({ storeList }) => (
  <div className="store-list">
    {storeList.map((store) => (
      <StoreListViewItem store={store} key={store.id}></StoreListViewItem>
    ))}
  </div>
);

export default StoreListView;

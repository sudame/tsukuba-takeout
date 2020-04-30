import React from 'react';
import { Store } from '../types';

type StoreListViewItemProps = {
  store: Store;
};

const StoreListViewItem: React.FC<StoreListViewItemProps> = ({ store }) => (
  <div className="store">
    <div className="store--name">{store.name}</div>
    <div className="store--genres">
      {store.genres.map((genre) => (
        <div key={genre.id} className="store--genre">
          {genre.name}
        </div>
      ))}
    </div>
    <div className="store--address">{store.address}</div>
    <div className="store--opening-hours">
      {store.opening_hours.map((openingHour) => (
        <div key={openingHour.id} className="store--genre">
          {openingHour.opening_time.slice(0, -3)} -{' '}
          {openingHour.closing_time.slice(0, -3)}
        </div>
      ))}
    </div>
    <div className="store--name">{store.short_description}</div>
    <div>
      <a href={store.url}>詳細</a>
    </div>
  </div>
);

export default StoreListViewItem;

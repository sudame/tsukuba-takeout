export type Store = {
  id: number;
  genres: StoreGenre[];
  area: StoreArea;
  name: string;
  slug: string;
  address: string;
  short_description: string;
  description: string;
  notice: string;
  opening_hours: StoreOpeningHour[];
  url: string;
};

export type StoreOpeningHour = {
  id: number;
  opening_time: string;
  closing_time: string;
};

export type StoreGenre = {
  id: number;
  name: string;
  slug: string;
};

export type StoreArea = {
  id: number;
  name: string;
  slug: string;
};

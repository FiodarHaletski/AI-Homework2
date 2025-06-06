/**
 * Geo coordinates for an address
 */
export interface Geo {
  lat: string;
  lng: string;
}

/**
 * Address information for a user
 */
export interface Address {
  street: string;
  suite: string;
  city: string;
  zipcode: string;
  geo: Geo;
}

/**
 * Company information for a user
 */
export interface Company {
  name: string;
  catchPhrase: string;
  bs: string;
}

/**
 * User object as returned by the API
 */
export interface User {
  id: number;
  name: string;
  username: string;
  email: string;
  address: Address;
  phone: string;
  website: string;
  company: Company;
} 
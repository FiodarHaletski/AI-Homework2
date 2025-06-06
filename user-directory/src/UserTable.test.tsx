import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import UserTable from './UserTable';
import { User } from './types';

const users: User[] = [
  {
    id: 1,
    name: 'Leanne Graham',
    username: 'Bret',
    email: 'Sincere@april.biz',
    address: {
      street: 'Kulas Light',
      suite: 'Apt. 556',
      city: 'Gwenborough',
      zipcode: '92998-3874',
      geo: { lat: '1', lng: '2' },
    },
    phone: '1-770-736-8031 x56442',
    website: 'hildegard.org',
    company: {
      name: 'Romaguera-Crona',
      catchPhrase: 'Multi-layered client-server neural-net',
      bs: 'harness real-time e-markets',
    },
  },
];

test('renders user table with data', () => {
  render(<UserTable users={users} onUserClick={jest.fn()} onDelete={jest.fn()} />);
  expect(screen.getByText('Leanne Graham')).toBeInTheDocument();
  expect(screen.getByText('Sincere@april.biz')).toBeInTheDocument();
  expect(screen.getByText('Romaguera-Crona')).toBeInTheDocument();
});

test('calls onUserClick when row is clicked', () => {
  const onUserClick = jest.fn();
  render(<UserTable users={users} onUserClick={onUserClick} onDelete={jest.fn()} />);
  fireEvent.click(screen.getByText('Leanne Graham'));
  expect(onUserClick).toHaveBeenCalledWith(users[0]);
});

test('calls onDelete when delete is clicked', () => {
  const onDelete = jest.fn();
  render(<UserTable users={users} onUserClick={jest.fn()} onDelete={onDelete} />);
  fireEvent.click(screen.getByTitle('Delete user'));
  expect(onDelete).toHaveBeenCalledWith(1);
}); 
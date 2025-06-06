import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import UserModal from './UserModal';
import { User } from './types';

const user: User = {
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
};

test('renders user modal with details', () => {
  render(<UserModal user={user} onClose={jest.fn()} />);
  expect(screen.getByText('Leanne Graham')).toBeInTheDocument();
  expect(screen.getByText('Sincere@april.biz')).toBeInTheDocument();
  expect(screen.getByText('Romaguera-Crona')).toBeInTheDocument();
  expect(screen.getByText('View on map')).toBeInTheDocument();
});

test('calls onClose when close button is clicked', () => {
  const onClose = jest.fn();
  render(<UserModal user={user} onClose={onClose} />);
  fireEvent.click(screen.getByText('×'));
  expect(onClose).toHaveBeenCalled();
});

test('calls onClose when overlay is clicked', () => {
  const onClose = jest.fn();
  render(<UserModal user={user} onClose={onClose} />);
  fireEvent.click(screen.getByTestId('modal-overlay'));
  expect(onClose).toHaveBeenCalled();
}); 
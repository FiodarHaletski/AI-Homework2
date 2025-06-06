import React from 'react';
import { User } from './types';
import styles from './UserDirectory.module.css';

interface UserTableProps {
  users: User[];
  onUserClick: (user: User) => void;
  onDelete: (id: number) => void;
}

/**
 * Table component for displaying a list of users.
 * @param users - Array of user objects
 * @param onUserClick - Callback when a user row is clicked
 * @param onDelete - Callback when delete action is triggered
 */
const UserTable: React.FC<UserTableProps> = ({ users, onUserClick, onDelete }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>Name / Email</th>
          <th>Address</th>
          <th>Phone</th>
          <th>Website</th>
          <th>Company</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        {users.map(user => (
          <tr key={user.id}>
            <td onClick={() => onUserClick(user)} style={{cursor: 'pointer'}}>
              <div><b>{user.name}</b></div>
              <div className={styles.email}>{user.email}</div>
            </td>
            <td onClick={() => onUserClick(user)} style={{cursor: 'pointer'}}>
              {user.address.city}, {user.address.street}
            </td>
            <td onClick={() => onUserClick(user)} style={{cursor: 'pointer'}}>{user.phone}</td>
            <td>
              <a href={`http://${user.website}`} className={styles.website} target="_blank" rel="noopener noreferrer">{user.website}</a>
            </td>
            <td onClick={() => onUserClick(user)} style={{cursor: 'pointer'}}>{user.company.name}</td>
            <td>
              <span className={styles.rowAction} title="Delete user" onClick={() => onDelete(user.id)}>&#10006;</span>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default UserTable; 
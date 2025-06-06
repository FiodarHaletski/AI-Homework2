import React from 'react';
import styles from './UserDirectory.module.css';
import { User } from './types';

interface UserModalProps {
  user: User;
  onClose: () => void;
}

/**
 * Modal component for displaying detailed user information.
 * @param user - The user to display
 * @param onClose - Callback to close the modal
 */
const UserModal: React.FC<UserModalProps> = ({ user, onClose }) => {
  const mapUrl = `https://www.google.com/maps?q=${user.address.geo.lat},${user.address.geo.lng}`;
  return (
    <div className={styles.modalOverlay} data-testid="modal-overlay" onClick={onClose}>
      <div className={styles.modal} onClick={e => e.stopPropagation()}>
        <button className={styles.closeBtn} onClick={onClose}>&times;</button>
        <div className={styles.modalTitle}>{user.name}</div>
        <div className={styles.modalSection}>
          <span className={styles.modalLabel}>Email: </span>
          <a href={`mailto:${user.email}`} className={styles.email}>{user.email}</a>
        </div>
        <div className={styles.modalSection}>
          <span className={styles.modalLabel}>Address: </span>
          {user.address.street}, {user.address.suite}<br/>
          {user.address.city}, {user.address.zipcode}
          <a href={mapUrl} className={styles.mapLink} target="_blank" rel="noopener noreferrer">View on map</a>
        </div>
        <div className={styles.modalSection}>
          <span className={styles.modalLabel}>Phone: </span>{user.phone}
        </div>
        <div className={styles.modalSection}>
          <span className={styles.modalLabel}>Website: </span>
          <a href={`http://${user.website}`} className={styles.website} target="_blank" rel="noopener noreferrer">{user.website}</a>
        </div>
        <div className={styles.modalSection}>
          <span className={styles.modalLabel}>Company: </span><br/>
          <b>Name:</b> {user.company.name}<br/>
          <b>Catchphrase:</b> {user.company.catchPhrase}<br/>
          <b>Business:</b> {user.company.bs}
        </div>
      </div>
    </div>
  );
};

export default UserModal; 
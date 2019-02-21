
ALTER TABLE `csv_db`.`player`
ADD CONSTRAINT `fk_body_type_id`
  FOREIGN KEY (`body_type_id`)
  REFERENCES `csv_db`.`body_type` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_country_id`
  FOREIGN KEY (`country_id`)
  REFERENCES `csv_db`.`country` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_club_id`
  FOREIGN KEY (`club_id`)
  REFERENCES `csv_db`.`club` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_preferred_foot_id`
  FOREIGN KEY (`preferred_foot_id`)
  REFERENCES `csv_db`.`preferred_foot` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

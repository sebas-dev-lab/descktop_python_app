from configurations.db.main import session, engine
from sqlalchemy.orm.exc import NoResultFound
from abc import ABC, abstractmethod
from sqlalchemy import and_, text


class Repository(ABC):
    def __init__(self, model):
        self.model = model
        self.session = session

    @abstractmethod
    def create(self, data_dict):
        try:
            instance = self.model(**data_dict)
            self.session.add(instance)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        
    @abstractmethod
    def update(self, filters, data_dict):
        try:
            filter_criteria=[]
            for key, value in filters.items():
                filter_criteria.append(getattr(self.model, key) == value)
            filter_condition=and_(*filter_criteria)
            self.session.query(self.model).filter(filter_condition).update(data_dict)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    @abstractmethod
    def delete_logical(self, model_id):
        try:
            self.update({'id': model_id}, {'is_deleted': True})
        except Exception as e:
            self.session.rollback()
            raise e

    @abstractmethod
    def delete_permanent(self, data_dict):
        try:
            filter_criteria=[]
            for key, value in data_dict.items():
                filter_criteria.append(getattr(self.model, key) == value)
            filter_condition=and_(*filter_criteria)
            self.session.query(self.model).filter(filter_condition).delete()
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    @abstractmethod
    def get_by_id(self, model_id):
        try:
            return self.session.query(self.model).filter_by(id=model_id, is_deleted=False).one()
        except NoResultFound:
            return None
        except Exception as e:
            raise e
        
    @abstractmethod
    def get_by_server_name(self, server_name):
        try:
            return self.session.query(self.model).filter_by(server_name=server_name, is_deleted=False).one()
        except NoResultFound:
            return None
        except Exception as e:
            raise e

    @abstractmethod
    def get_all(self):
        try:
            return self.session.query(self.model).filter_by(is_deleted=False).order_by(self.model.created_at).all()
        except Exception as e:
            raise e

    @abstractmethod
    def get_all_paginated(self, page=1, per_page=10):
        try:
            query = self.session.query(self.model).filter_by(is_deleted=False)
            total = query.count()
            items = query.limit(per_page).offset((page - 1) * per_page).all()
            return items, total
        except Exception as e:
            raise e
    
    @abstractmethod
    def query(self, query_string, params):
        try:
            print(params)
            with self.session.connection() as connection:
                return connection.execute(text(query_string), params).fetchall()
        except Exception as e:
            raise e

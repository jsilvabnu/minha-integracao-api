from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    email = Column(String(128), unique=True, nullable=False, index=True)
    password_hash = Column(String(256), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Polymorphic identity
    user_type = Column(String(50))

    # Relationships for Borrow model
    borrowed_items = relationship("Borrow", foreign_keys="Borrow.borrower_id", back_populates="borrower", lazy="dynamic")
    processed_loans = relationship("Borrow", foreign_keys="Borrow.lender_id", back_populates="lender", lazy="dynamic")

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': user_type
    }

class Funcionario(User):
    __tablename__ = "funcionario"

    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    role = Column(String(100), nullable=False)  # Cargo

    __mapper_args__ = {
        'polymorphic_identity': 'funcionario',
    }

class Cliente(User):
    __tablename__ = "cliente"

    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    customer_type = Column(String(50))  # e.g., 'individual', 'corporate'
    address = Column(String(255)) # Endereço

    __mapper_args__ = {
        'polymorphic_identity': 'cliente',
    }

"""Criar tabelas atividade e usuarios

Revision ID: 58c1f13ae98e
Revises: 
Create Date: 2025-07-08 10:28:06.184081

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '58c1f13ae98e'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('atividade',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descricao', sa.Text(), nullable=True),
        sa.Column('data_criacao', sa.Date(), nullable=True),
        sa.Column('data_prevista', sa.Date(), nullable=True),
        sa.Column('data_encerramento', sa.Date(), nullable=True),
        sa.Column('situacao', sa.String(length=50), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuarios',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(length=100), nullable=True),
        sa.Column('email', sa.String(length=150), nullable=True),
        sa.Column('senha', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('usuarios')
    op.drop_table('atividade')


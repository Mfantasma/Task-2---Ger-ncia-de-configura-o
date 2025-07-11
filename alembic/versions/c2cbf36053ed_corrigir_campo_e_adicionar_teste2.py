"""Corrigir campo e adicionar teste2

Revision ID: c2cbf36053ed
Revises: 4d59442cffa7
Create Date: 2025-07-08 18:50:10.529774

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c2cbf36053ed'
down_revision: Union[str, Sequence[str], None] = '4d59442cffa7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teste2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('atividade', sa.Column('data_prevista', sa.Date(), nullable=True))
    op.drop_column('atividade', 'data_previsa')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('atividade', sa.Column('data_previsa', sa.DATE(), autoincrement=False, nullable=True))
    op.drop_column('atividade', 'data_prevista')
    op.drop_table('teste2')
    # ### end Alembic commands ###

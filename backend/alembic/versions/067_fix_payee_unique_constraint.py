"""fix_payee_unique_constraint

Revision ID: 7070a43ce403
Revises: 065
Create Date: 2026-08-12 13:07:42.283096

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '067'
down_revision: Union[str, Sequence[str], None] = '066'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_constraint('uq_payees_user_id_name', 'payees', type_='unique')
    op.create_unique_constraint('uq_payees_workspace_id_name', 'payees', ['workspace_id', 'name'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('uq_payees_workspace_id_name', 'payees', type_='unique')
    op.create_unique_constraint('uq_payees_user_id_name', 'payees', ['user_id', 'name'])

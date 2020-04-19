"""empty message

Revision ID: 92baf66b268b
Revises: 224fd8963462
Create Date: 2020-03-30 17:48:21.584864

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92baf66b268b'
down_revision = '224fd8963462'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('email_log', sa.Column('is_spam', sa.Boolean(), server_default='0', nullable=False))
    op.add_column('email_log', sa.Column('spam_status', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('email_log', 'spam_status')
    op.drop_column('email_log', 'is_spam')
    # ### end Alembic commands ###
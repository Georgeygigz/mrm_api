"""include cascading deletion

Revision ID: ab83c84a325b
Revises: 7747e8e2c4ac
Create Date: 2019-02-12 11:54:49.151206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab83c84a325b'
down_revision = '7747e8e2c4ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('blocks_office_id_fkey', 'blocks', type_='foreignkey')
    op.create_foreign_key(None, 'blocks', 'offices', ['office_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('devices_room_id_fkey', 'devices', type_='foreignkey')
    op.create_foreign_key(None, 'devices', 'rooms', ['room_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('events_room_id_fkey', 'events', type_='foreignkey')
    op.create_foreign_key(None, 'events', 'rooms', ['room_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('floors_block_id_fkey', 'floors', type_='foreignkey')
    op.create_foreign_key(None, 'floors', 'blocks', ['block_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('notifications_user_id_fkey', 'notifications', type_='foreignkey')
    op.create_foreign_key(None, 'notifications', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('offices_location_id_fkey', 'offices', type_='foreignkey')
    op.create_foreign_key(None, 'offices', 'locations', ['location_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('resources_room_id_fkey', 'resources', type_='foreignkey')
    op.create_foreign_key(None, 'resources', 'rooms', ['room_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('responses_question_id_fkey', 'responses', type_='foreignkey')
    op.drop_constraint('responses_room_id_fkey', 'responses', type_='foreignkey')
    op.create_foreign_key(None, 'responses', 'questions', ['question_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'responses', 'rooms', ['room_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('rooms_floor_id_fkey', 'rooms', type_='foreignkey')
    op.drop_constraint('rooms_wing_id_fkey', 'rooms', type_='foreignkey')
    op.drop_constraint('rooms_location_id_fkey', 'rooms', type_='foreignkey')
    op.create_foreign_key(None, 'rooms', 'floors', ['floor_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'rooms', 'wings', ['wing_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'rooms', 'locations', ['location_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('users_roles_user_id_fkey', 'users_roles', type_='foreignkey')
    op.drop_constraint('users_roles_role_id_fkey', 'users_roles', type_='foreignkey')
    op.create_foreign_key(None, 'users_roles', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'users_roles', 'roles', ['role_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('wings_floor_id_fkey', 'wings', type_='foreignkey')
    op.create_foreign_key(None, 'wings', 'floors', ['floor_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'wings', type_='foreignkey')
    op.create_foreign_key('wings_floor_id_fkey', 'wings', 'floors', ['floor_id'], ['id'])
    op.drop_constraint(None, 'users_roles', type_='foreignkey')
    op.drop_constraint(None, 'users_roles', type_='foreignkey')
    op.create_foreign_key('users_roles_role_id_fkey', 'users_roles', 'roles', ['role_id'], ['id'])
    op.create_foreign_key('users_roles_user_id_fkey', 'users_roles', 'users', ['user_id'], ['id'])
    op.drop_constraint(None, 'rooms', type_='foreignkey')
    op.drop_constraint(None, 'rooms', type_='foreignkey')
    op.drop_constraint(None, 'rooms', type_='foreignkey')
    op.create_foreign_key('rooms_location_id_fkey', 'rooms', 'locations', ['location_id'], ['id'])
    op.create_foreign_key('rooms_wing_id_fkey', 'rooms', 'wings', ['wing_id'], ['id'])
    op.create_foreign_key('rooms_floor_id_fkey', 'rooms', 'floors', ['floor_id'], ['id'])
    op.drop_constraint(None, 'responses', type_='foreignkey')
    op.drop_constraint(None, 'responses', type_='foreignkey')
    op.create_foreign_key('responses_room_id_fkey', 'responses', 'rooms', ['room_id'], ['id'])
    op.create_foreign_key('responses_question_id_fkey', 'responses', 'questions', ['question_id'], ['id'])
    op.drop_constraint(None, 'resources', type_='foreignkey')
    op.create_foreign_key('resources_room_id_fkey', 'resources', 'rooms', ['room_id'], ['id'])
    op.drop_constraint(None, 'offices', type_='foreignkey')
    op.create_foreign_key('offices_location_id_fkey', 'offices', 'locations', ['location_id'], ['id'])
    op.drop_constraint(None, 'notifications', type_='foreignkey')
    op.create_foreign_key('notifications_user_id_fkey', 'notifications', 'users', ['user_id'], ['id'])
    op.drop_constraint(None, 'floors', type_='foreignkey')
    op.create_foreign_key('floors_block_id_fkey', 'floors', 'blocks', ['block_id'], ['id'])
    op.drop_constraint(None, 'events', type_='foreignkey')
    op.create_foreign_key('events_room_id_fkey', 'events', 'rooms', ['room_id'], ['id'])
    op.drop_constraint(None, 'devices', type_='foreignkey')
    op.create_foreign_key('devices_room_id_fkey', 'devices', 'rooms', ['room_id'], ['id'])
    op.drop_constraint(None, 'blocks', type_='foreignkey')
    op.create_foreign_key('blocks_office_id_fkey', 'blocks', 'offices', ['office_id'], ['id'])
    # ### end Alembic commands ###

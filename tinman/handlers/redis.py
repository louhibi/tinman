"""The RedisRequestHandler uses tornado-redis to support Redis. It will
auto-establish a single redis connection when initializing the connection.

"""
import logging
import tornadoredis
from tornado import gen
from tornado import web

LOGGER = logging.getLogger(__name__)

from tinman import exceptions

class RedisRequestHandler(web.RequestHandler):
    """This request handler will connect to Redis on initialize if the
    connection is not previously set.

    """
    REDIS_CLIENT = 'redis'
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0

    def prepare(self):
        super(RedisRequestHandler, self).prepare()
        if not self._has_redis_client:
            self._set_redis_client(self._connect_to_redis())

        LOGGER.debug('Redis client: %r', self._redis_client)

    @property
    def _has_redis_client(self):
        return hasattr(self.application.tinman, self.REDIS_CLIENT)

    def _connect_to_redis(self):
        LOGGER.debug('Connecting to redis')
        return tornadoredis.Client(**self._redis_connection_settings)

    @property
    def _redis_connection_settings(self):
        LOGGER.debug('Redis arguments')
        return {'host': self._redis_settings.get('host', self.REDIS_HOST),
                'port': self._redis_settings.get('port', self.REDIS_PORT),
                'selected_db': self._redis_settings.get('db', self.REDIS_DB)}

    @property
    def _redis_client(self):
        LOGGER.debug('Returning redis client')
        return getattr(self.application.tinman, self.REDIS_CLIENT, None)

    @property
    def _redis_settings(self):
        LOGGER.debug('Redis settings')
        return self.application.settings.get('redis', dict())

    def _set_redis_client(self, client):
        setattr(self.application.tinman, self.REDIS_CLIENT, client)

    ## Autogenerated methods
    @gen.engine
    def _redis_append(self, key, value):
        """Append a value to a key

        :param str key: key
        :param str value: string

        """
        yield gen.Task(self._redis_client.append, key, value)

    @gen.engine
    def _redis_bitcount(self, key, start, end):
        """Count set bits in a string

        :param str key: key
        :param int start: integer
        :param int end: integer

        """
        yield gen.Task(self._redis_client.bitcount, key, start, end)

    @gen.engine
    def _redis_bitop(self, operation, destkey, key):
        """Perform bitwise operations between strings

        :param str operation: string
        :param str destkey: key
        :param str key: key

        """
        yield gen.Task(self._redis_client.bitop, operation, destkey, key)

    @gen.engine
    def _redis_blpop(self, key, timeout):
        """Remove and get the first element in a list, or block until one is
        available

        :param str key: key
        :param int timeout: integer

        """
        yield gen.Task(self._redis_client.blpop, key, timeout)

    @gen.engine
    def _redis_brpop(self, key, timeout):
        """Remove and get the last element in a list, or block until one is
        available

        :param str key: key
        :param int timeout: integer

        """
        yield gen.Task(self._redis_client.brpop, key, timeout)

    @gen.engine
    def _redis_brpoplpush(self, source, destination, timeout):
        """Pop a value from a list, push it to another list and return it; or
        block until one is available

        :param str source: key
        :param str destination: key
        :param int timeout: integer

        """
        yield gen.Task(self._redis_client.brpoplpush, source, destination,
                       timeout)

    @gen.engine
    def _redis_decr(self, key):
        """Decrement the integer value of a key by one

        :param str key: key

        """
        yield gen.Task(self._redis_client.decr, key)

    @gen.engine
    def _redis_decrby(self, key, decrement):
        """Decrement the integer value of a key by the given number

        :param str key: key
        :param int decrement: integer

        """
        yield gen.Task(self._redis_client.decrby, key, decrement)

    @gen.engine
    def _redis_delete(self, key):
        """Delete a key

        :param str key: key

        """
        yield gen.Task(self._redis_client.delete, key)

    @gen.engine
    def _redis_discard(self):
        """Discard all commands issued after MULTI

        """
        yield gen.Task(self._redis_client.discard)

    @gen.engine
    def _redis_dump(self, key):
        """Return a serialized version of the value stored at the specified key.

        :param str key: key

        """
        yield gen.Task(self._redis_client.dump, key)

    @gen.engine
    def _redis_eval(self, script, numkeys, key, arg):
        """Execute a Lua script server side

        :param str script: string
        :param int numkeys: integer
        :param str key: key
        :param str arg: string

        """
        yield gen.Task(self._redis_client.eval, script, numkeys, key, arg)

    @gen.engine
    def _redis_evalsha(self, sha1, numkeys, key, arg):
        """Execute a Lua script server side

        :param str sha1: string
        :param int numkeys: integer
        :param str key: key
        :param str arg: string

        """
        yield gen.Task(self._redis_client.evalsha, sha1, numkeys, key, arg)

    @gen.engine
    def _redis_execute(self):
        """Execute all commands issued after MULTI

        """
        yield gen.Task(self._redis_client.execute)

    @gen.engine
    def _redis_exists(self, key):
        """Determine if a key exists

        :param str key: key

        """
        yield gen.Task(self._redis_client.exists, key)

    @gen.engine
    def _redis_expire(self, key, seconds):
        """Set a key's time to live in seconds

        :param str key: key
        :param int seconds: integer

        """
        yield gen.Task(self._redis_client.expire, key, seconds)

    @gen.engine
    def _redis_expireat(self, key, timestamp):
        """Set the expiration for a key as a UNIX timestamp

        :param str key: key
        :param int timestamp: posix time

        """
        yield gen.Task(self._redis_client.expireat, key, timestamp)

    @gen.engine
    def _redis_get(self, key):
        """Get the value of a key

        :param str key: key

        """
        yield gen.Task(self._redis_client.get, key)

    @gen.engine
    def _redis_getbit(self, key, offset):
        """Returns the bit value at offset in the string value stored at key

        :param str key: key
        :param int offset: integer

        """
        yield gen.Task(self._redis_client.getbit, key, offset)

    @gen.engine
    def _redis_getrange(self, key, start, end):
        """Get a substring of the string stored at a key

        :param str key: key
        :param int start: integer
        :param int end: integer

        """
        yield gen.Task(self._redis_client.getrange, key, start, end)

    @gen.engine
    def _redis_getset(self, key, value):
        """Set the string value of a key and return its old value

        :param str key: key
        :param str value: string

        """
        yield gen.Task(self._redis_client.getset, key, value)

    @gen.engine
    def _redis_hdel(self, key, field):
        """Delete one or more hash fields

        :param str key: key
        :param str field: string

        """
        yield gen.Task(self._redis_client.hdel, key, field)

    @gen.engine
    def _redis_hexists(self, key, field):
        """Determine if a hash field exists

        :param str key: key
        :param str field: string

        """
        yield gen.Task(self._redis_client.hexists, key, field)

    @gen.engine
    def _redis_hget(self, key, field):
        """Get the value of a hash field

        :param str key: key
        :param str field: string

        """
        yield gen.Task(self._redis_client.hget, key, field)

    @gen.engine
    def _redis_hgetall(self, key):
        """Get all the fields and values in a hash

        :param str key: key

        """
        yield gen.Task(self._redis_client.hgetall, key)

    @gen.engine
    def _redis_hincrby(self, key, field, increment):
        """Increment the integer value of a hash field by the given number

        :param str key: key
        :param str field: string
        :param int increment: integer

        """
        yield gen.Task(self._redis_client.hincrby, key, field, increment)

    @gen.engine
    def _redis_hincrbyfloat(self, key, field, increment):
        """Increment the float value of a hash field by the given amount

        :param str key: key
        :param str field: string
        :param float increment: double

        """
        yield gen.Task(self._redis_client.hincrbyfloat, key, field, increment)

    @gen.engine
    def _redis_hkeys(self, key):
        """Get all the fields in a hash

        :param str key: key

        """
        yield gen.Task(self._redis_client.hkeys, key)

    @gen.engine
    def _redis_hlen(self, key):
        """Get the number of fields in a hash

        :param str key: key

        """
        yield gen.Task(self._redis_client.hlen, key)

    @gen.engine
    def _redis_hmget(self, key, field):
        """Get the values of all the given hash fields

        :param str key: key
        :param str field: string

        """
        yield gen.Task(self._redis_client.hmget, key, field)

    @gen.engine
    def _redis_hmset(self, key, mapping):
        """Set multiple hash fields to multiple values

        :param str key: key
        :param list mapping: the item mapping

        """
        yield gen.Task(self._redis_client.hmset, key, mapping)

    @gen.engine
    def _redis_hset(self, key, field, value):
        """Set the string value of a hash field

        :param str key: key
        :param str field: string
        :param str value: string

        """
        yield gen.Task(self._redis_client.hset, key, field, value)

    @gen.engine
    def _redis_hsetnx(self, key, field, value):
        """Set the value of a hash field, only if the field does not exist

        :param str key: key
        :param str field: string
        :param str value: string

        """
        yield gen.Task(self._redis_client.hsetnx, key, field, value)

    @gen.engine
    def _redis_hvals(self, key):
        """Get all the values in a hash

        :param str key: key

        """
        yield gen.Task(self._redis_client.hvals, key)

    @gen.engine
    def _redis_incr(self, key):
        """Increment the integer value of a key by one

        :param str key: key

        """
        yield gen.Task(self._redis_client.incr, key)

    @gen.engine
    def _redis_incrby(self, key, increment):
        """Increment the integer value of a key by the given amount

        :param str key: key
        :param int increment: integer

        """
        yield gen.Task(self._redis_client.incrby, key, increment)

    @gen.engine
    def _redis_incrbyfloat(self, key, increment):
        """Increment the float value of a key by the given amount

        :param str key: key
        :param float increment: double

        """
        yield gen.Task(self._redis_client.incrbyfloat, key, increment)

    @gen.engine
    def _redis_keys(self, pattern):
        """Find all keys matching the given pattern

        :param str pattern: pattern

        """
        yield gen.Task(self._redis_client.keys, pattern)

    @gen.engine
    def _redis_lindex(self, key, index):
        """Get an element from a list by its index

        :param str key: key
        :param int index: integer

        """
        yield gen.Task(self._redis_client.lindex, key, index)

    @gen.engine
    def _redis_linsert(self, key, where, pivot, value):
        """Insert an element before or after another element in a list

        :param str key: key
        :param tuple where: enum
        :param str pivot: string
        :param str value: string

        """
        yield gen.Task(self._redis_client.linsert, key, where, pivot, value)

    @gen.engine
    def _redis_llen(self, key):
        """Get the length of a list

        :param str key: key

        """
        yield gen.Task(self._redis_client.llen, key)

    @gen.engine
    def _redis_lpop(self, key):
        """Remove and get the first element in a list

        :param str key: key

        """
        yield gen.Task(self._redis_client.lpop, key)

    @gen.engine
    def _redis_lpush(self, key, value):
        """Prepend one or multiple values to a list

        :param str key: key
        :param str value: string

        """
        yield gen.Task(self._redis_client.lpush, key, value)

    @gen.engine
    def _redis_lpushx(self, key, value):
        """Prepend a value to a list, only if the list exists

        :param str key: key
        :param str value: string

        """
        yield gen.Task(self._redis_client.lpushx, key, value)

    @gen.engine
    def _redis_lrange(self, key, start, stop):
        """Get a range of elements from a list

        :param str key: key
        :param int start: integer
        :param int stop: integer

        """
        yield gen.Task(self._redis_client.lrange, key, start, stop)

    @gen.engine
    def _redis_lrem(self, key, count, value):
        """Remove elements from a list

        :param str key: key
        :param int count: integer
        :param str value: string

        """
        yield gen.Task(self._redis_client.lrem, key, count, value)

    @gen.engine
    def _redis_lset(self, key, index, value):
        """Set the value of an element in a list by its index

        :param str key: key
        :param int index: integer
        :param str value: string

        """
        yield gen.Task(self._redis_client.lset, key, index, value)

    @gen.engine
    def _redis_ltrim(self, key, start, stop):
        """Trim a list to the specified range

        :param str key: key
        :param int start: integer
        :param int stop: integer

        """
        yield gen.Task(self._redis_client.ltrim, key, start, stop)

    @gen.engine
    def _redis_mget(self, key):
        """Get the values of all the given keys

        :param str key: key

        """
        yield gen.Task(self._redis_client.mget, key)

    @gen.engine
    def _redis_migrate(self, host, port, key, destination_db, timeout):
        """Atomically transfer a key from a Redis instance to another one.

        :param str host: string
        :param str port: string
        :param str key: key
        :param int destination-db: integer
        :param int timeout: integer

        """
        yield gen.Task(self._redis_client.migrate, host, port, key,
                       destination_db, timeout)

    @gen.engine
    def _redis_move(self, key, db):
        """Move a key to another database

        :param str key: key
        :param int db: integer

        """
        yield gen.Task(self._redis_client.move, key, db)

    @gen.engine
    def _redis_mset(self, key, value):
        """Set multiple keys to multiple values

        :param ['str', 'str'] [u'key', u'value']: string

        """
        yield gen.Task(self._redis_client.mset, key, value)

    @gen.engine
    def _redis_msetnx(self, key, value):
        """Set multiple keys to multiple values, only if none of the keys exist

        :param ['str', 'str'] [u'key', u'value']: string

        """
        yield gen.Task(self._redis_client.msetnx, key, value)

    @gen.engine
    def _redis_multi(self):
        """Mark the start of a transaction block

        """
        yield gen.Task(self._redis_client.multi)

    @gen.engine
    def _redis_object(self, subcommand, arguments):
        """Inspect the internals of Redis objects

        :param str subcommand: string
        :param str arguments: string

        """
        yield gen.Task(self._redis_client.object, subcommand, arguments)

    @gen.engine
    def _redis_persist(self, key):
        """Remove the expiration from a key

        :param str key: key

        """
        yield gen.Task(self._redis_client.persist, key)

    @gen.engine
    def _redis_pexpire(self, key, milliseconds):
        """Set a key's time to live in milliseconds

        :param str key: key
        :param int milliseconds: integer

        """
        yield gen.Task(self._redis_client.pexpire, key, milliseconds)

    @gen.engine
    def _redis_pexpireat(self, key, milliseconds_timestamp):
        """Set the expiration for a key as a UNIX timestamp specified in
        milliseconds

        :param str key: key
        :param int milliseconds-timestamp: posix time

        """
        yield gen.Task(self._redis_client.pexpireat, key,
                       milliseconds_timestamp)

    @gen.engine
    def _redis_psetex(self, key, milliseconds, value):
        """Set the value and expiration in milliseconds of a key

        :param str key: key
        :param int milliseconds: integer
        :param str value: string

        """
        yield gen.Task(self._redis_client.psetex, key, milliseconds, value)

    @gen.engine
    def _redis_psubscribe(self, pattern):
        """Listen for messages published to channels matching the given patterns

        :param ['str'] [u'pattern']: pattern

        """
        yield gen.Task(self._redis_client.psubscribe, pattern)

    @gen.engine
    def _redis_pttl(self, key):
        """Get the time to live for a key in milliseconds

        :param str key: key

        """
        yield gen.Task(self._redis_client.pttl, key)

    @gen.engine
    def _redis_publish(self, channel, message):
        """Post a message to a channel

        :param str channel: string
        :param str message: string

        """
        yield gen.Task(self._redis_client.publish, channel, message)

    @gen.engine
    def _redis_punsubscribe(self, pattern):
        """Stop listening for messages posted to channels matching the given
        patterns

        :param str pattern: pattern

        """
        yield gen.Task(self._redis_client.punsubscribe, pattern)

    @gen.engine
    def _redis_randomkey(self):
        """Return a random key from the keyspace

        """
        yield gen.Task(self._redis_client.randomkey)

    @gen.engine
    def _redis_rename(self, key, newkey):
        """Rename a key

        :param str key: key
        :param str newkey: key

        """
        yield gen.Task(self._redis_client.rename, key, newkey)

    @gen.engine
    def _redis_renamenx(self, key, newkey):
        """Rename a key, only if the new key does not exist

        :param str key: key
        :param str newkey: key

        """
        yield gen.Task(self._redis_client.renamenx, key, newkey)

    @gen.engine
    def _redis_restore(self, key, ttl, serialized_value):
        """Create a key using the provided serialized value, previously
        obtained using DUMP.

        :param str key: key
        :param int ttl: integer
        :param str serialized-value: string

        """
        yield gen.Task(self._redis_client.restore, key, ttl, serialized_value)

    @gen.engine
    def _redis_rpop(self, key):
        """Remove and get the last element in a list

        :param str key: key

        """
        yield gen.Task(self._redis_client.rpop, key)

    @gen.engine
    def _redis_rpoplpush(self, source, destination):
        """Remove the last element in a list, append it to another list and
        return it

        :param str source: key
        :param str destination: key

        """
        yield gen.Task(self._redis_client.rpoplpush, source, destination)

    @gen.engine
    def _redis_rpush(self, key, value):
        """Append one or multiple values to a list

        :param str key: key
        :param str value: string

        """
        yield gen.Task(self._redis_client.rpush, key, value)

    @gen.engine
    def _redis_rpushx(self, key, value):
        """Append a value to a list, only if the list exists

        :param str key: key
        :param str value: string

        """
        yield gen.Task(self._redis_client.rpushx, key, value)

    @gen.engine
    def _redis_sadd(self, key, member):
        """Add one or more members to a set

        :param str key: key
        :param str member: string

        """
        yield gen.Task(self._redis_client.sadd, key, member)

    @gen.engine
    def _redis_scard(self, key):
        """Get the number of members in a set

        :param str key: key

        """
        yield gen.Task(self._redis_client.scard, key)

    @gen.engine
    def _redis_script_exists(self, script):
        """Check existence of scripts in the script cache.

        :param str script: string

        """
        yield gen.Task(self._redis_client.script_exists, script)

    @gen.engine
    def _redis_script_flush(self):
        """Remove all the scripts from the script cache.

        """
        yield gen.Task(self._redis_client.script_flush)

    @gen.engine
    def _redis_script_kill(self):
        """Kill the script currently in execution.

        """
        yield gen.Task(self._redis_client.script_kill)

    @gen.engine
    def _redis_script_load(self, script):
        """Load the specified Lua script into the script cache.

        :param str script: string

        """
        yield gen.Task(self._redis_client.script_load, script)

    @gen.engine
    def _redis_sdiff(self, key):
        """Subtract multiple sets

        :param str key: key

        """
        yield gen.Task(self._redis_client.sdiff, key)

    @gen.engine
    def _redis_sdiffstore(self, destination, key):
        """Subtract multiple sets and store the resulting set in a key

        :param str destination: key
        :param str key: key

        """
        yield gen.Task(self._redis_client.sdiffstore, destination, key)

    @gen.engine
    def _redis_set(self, key, value):
        """Set the string value of a key

        :param str key: key
        :param str value: string

        """
        LOGGER.debug('Redis settings: %s', key)
        yield gen.Task(self._redis_client.set, key, value)

    @gen.engine
    def _redis_setbit(self, key, offset, value):
        """Sets or clears the bit at offset in the string value stored at key

        :param str key: key
        :param int offset: integer
        :param str value: string

        """
        yield gen.Task(self._redis_client.setbit, key, offset, value)

    @gen.engine
    def _redis_setex(self, key, seconds, value):
        """Set the value and expiration of a key

        :param str key: key
        :param int seconds: integer
        :param str value: string

        """
        yield gen.Task(self._redis_client.setex, key, seconds, value)

    @gen.engine
    def _redis_setnx(self, key, value):
        """Set the value of a key, only if the key does not exist

        :param str key: key
        :param str value: string

        """
        yield gen.Task(self._redis_client.setnx, key, value)

    @gen.engine
    def _redis_setrange(self, key, offset, value):
        """Overwrite part of a string at key starting at the specified offset

        :param str key: key
        :param int offset: integer
        :param str value: string

        """
        yield gen.Task(self._redis_client.setrange, key, offset, value)

    @gen.engine
    def _redis_sinter(self, key):
        """Intersect multiple sets

        :param str key: key

        """
        yield gen.Task(self._redis_client.sinter, key)

    @gen.engine
    def _redis_sinterstore(self, destination, key):
        """Intersect multiple sets and store the resulting set in a key

        :param str destination: key
        :param str key: key

        """
        yield gen.Task(self._redis_client.sinterstore, destination, key)

    @gen.engine
    def _redis_sismember(self, key, member):
        """Determine if a given value is a member of a set

        :param str key: key
        :param str member: string

        """
        yield gen.Task(self._redis_client.sismember, key, member)

    @gen.engine
    def _redis_smembers(self, key):
        """Get all the members in a set

        :param str key: key

        """
        yield gen.Task(self._redis_client.smembers, key)

    @gen.engine
    def _redis_smove(self, source, destination, member):
        """Move a member from one set to another

        :param str source: key
        :param str destination: key
        :param str member: string

        """
        yield gen.Task(self._redis_client.smove, source, destination, member)

    @gen.engine
    def _redis_sort(self, key, start=None, num=None, by=None, get=None,
                    desc=False, alpha=False, store=None):
        """Sort the elements in a list, set or sorted set"""
        yield gen.Task(self._redis_client.sort, key, start, num, by, get, desc,
                       alpha, store)

    @gen.engine
    def _redis_spop(self, key):
        """Remove and return a random member from a set

        :param str key: key

        """
        yield gen.Task(self._redis_client.spop, key)

    @gen.engine
    def _redis_srandmember(self, key, count):
        """Get one or multiple random members from a set

        :param str key: key
        :param int count: integer

        """
        yield gen.Task(self._redis_client.srandmember, key, count)

    @gen.engine
    def _redis_srem(self, key, member):
        """Remove one or more members from a set

        :param str key: key
        :param str member: string

        """
        yield gen.Task(self._redis_client.srem, key, member)

    @gen.engine
    def _redis_strlen(self, key):
        """Get the length of the value stored in a key

        :param str key: key

        """
        yield gen.Task(self._redis_client.strlen, key)

    @gen.engine
    def _redis_subscribe(self, channel):
        """Listen for messages published to the given channels

        :param ['str'] [u'channel']: string

        """
        yield gen.Task(self._redis_client.subscribe, channel)

    @gen.engine
    def _redis_sunion(self, key):
        """Add multiple sets

        :param str key: key

        """
        yield gen.Task(self._redis_client.sunion, key)

    @gen.engine
    def _redis_sunionstore(self, destination, key):
        """Add multiple sets and store the resulting set in a key

        :param str destination: key
        :param str key: key

        """
        yield gen.Task(self._redis_client.sunionstore, destination, key)

    @gen.engine
    def _redis_ttl(self, key):
        """Get the time to live for a key

        :param str key: key

        """
        yield gen.Task(self._redis_client.ttl, key)

    @gen.engine
    def _redis_type(self, key):
        """Determine the type stored at key

        :param str key: key

        """
        yield gen.Task(self._redis_client.type, key)

    @gen.engine
    def _redis_unsubscribe(self, channel):
        """Stop listening for messages posted to the given channels

        :param str channel: string

        """
        yield gen.Task(self._redis_client.unsubscribe, channel)

    @gen.engine
    def _redis_unwatch(self):
        """Forget about all watched keys

        """
        yield gen.Task(self._redis_client.unwatch)

    @gen.engine
    def _redis_watch(self, key):
        """Watch the given keys to determine execution of the MULTI/EXEC block

        :param str key: key

        """
        yield gen.Task(self._redis_client.watch, key)

    @gen.engine
    def _redis_zadd(self, key, score, value):
        """Add one or more members to a sorted set, or update its score if it
        already exists

        :param str key: key
        :param float score: double
        :param str value: string

        """
        yield gen.Task(self._redis_client.zadd, key, score, value)

    @gen.engine
    def _redis_zcard(self, key):
        """Get the number of members in a sorted set

        :param str key: key

        """
        yield gen.Task(self._redis_client.zcard, key)

    @gen.engine
    def _redis_zcount(self, key, min, max):
        """Count the members in a sorted set with scores within the given values

        :param str key: key
        :param float min: double
        :param float max: double

        """
        yield gen.Task(self._redis_client.zcount, key, min, max)

    @gen.engine
    def _redis_zincrby(self, key, increment, member):
        """Increment the score of a member in a sorted set

        :param str key: key
        :param int increment: integer
        :param str member: string

        """
        yield gen.Task(self._redis_client.zincrby, key, increment, member)

    @gen.engine
    def _redis_zinterstore(self, destination, numkeys, key, weight, aggregate):
        """Intersect multiple sorted sets and store the resulting sorted set
        in a new key

        :param str destination: key
        :param int numkeys: integer
        :param str key: key
        :param int weight: integer
        :param tuple aggregate: enum

        """
        yield gen.Task(self._redis_client.zinterstore, destination, numkeys,
                       key, weight, aggregate)

    @gen.engine
    def _redis_zrange(self, key, start, stop, withscores):
        """Return a range of members in a sorted set, by index

        :param str key: key
        :param int start: integer
        :param int stop: integer
        :param tuple withscores: enum

        """
        yield gen.Task(self._redis_client.zrange, key, start, stop, withscores)

    @gen.engine
    def _redis_zrangebyscore(self, key, min, max, withscores, offset, count):
        """Return a range of members in a sorted set, by score

        :param str key: key
        :param float min: double
        :param float max: double
        :param tuple withscores: enum
        :param int offset: offset
        :param int count: count

        """
        yield gen.Task(self._redis_client.zrangebyscore, key, min, max,
                       withscores, offset, count)

    @gen.engine
    def _redis_zrank(self, key, member):
        """Determine the index of a member in a sorted set

        :param str key: key
        :param str member: string

        """
        yield gen.Task(self._redis_client.zrank, key, member)

    @gen.engine
    def _redis_zrem(self, key, member):
        """Remove one or more members from a sorted set

        :param str key: key
        :param str member: string

        """
        yield gen.Task(self._redis_client.zrem, key, member)

    @gen.engine
    def _redis_zremrangebyrank(self, key, start, stop):
        """Remove all members in a sorted set within the given indexes

        :param str key: key
        :param int start: integer
        :param int stop: integer

        """
        yield gen.Task(self._redis_client.zremrangebyrank, key, start, stop)

    @gen.engine
    def _redis_zremrangebyscore(self, key, min, max):
        """Remove all members in a sorted set within the given scores

        :param str key: key
        :param float min: double
        :param float max: double

        """
        yield gen.Task(self._redis_client.zremrangebyscore, key, min, max)

    @gen.engine
    def _redis_zrevrange(self, key, start, stop, withscores):
        """Return a range of members in a sorted set, by index, with scores
        ordered from high to low

        :param str key: key
        :param int start: integer
        :param int stop: integer
        :param tuple withscores: enum

        """
        yield gen.Task(self._redis_client.zrevrange, key, start, stop,
                       withscores)

    @gen.engine
    def _redis_zrevrangebyscore(self, key, max, min, withscores, offset,
                                count):
        """Return a range of members in a sorted set, by score, with scores
        ordered from high to low

        :param str key: key
        :param float max: double
        :param float min: double
        :param tuple withscores: enum
        :param ['int', 'int'] [u'offset', u'count']: integer

        """
        yield gen.Task(self._redis_client.zrevrangebyscore, key, max, min,
                       withscores, offset, count)

    @gen.engine
    def _redis_zrevrank(self, key, member):
        """Determine the index of a member in a sorted set, with scores
        ordered from high to low

        :param str key: key
        :param str member: string

        """
        yield gen.Task(self._redis_client.zrevrank, key, member)

    @gen.engine
    def _redis_zscore(self, key, member):
        """Get the score associated with the given member in a sorted set

        :param str key: key
        :param str member: string

        """
        yield gen.Task(self._redis_client.zscore, key, member)

    @gen.engine
    def _redis_zunionstore(self, destination, numkeys, key, weight, aggregate):
        """Add multiple sorted sets and store the resulting sorted set in a
        new key

        :param str destination: key
        :param int numkeys: integer
        :param str key: key
        :param int weight: integer
        :param tuple aggregate: enum

        """
        yield gen.Task(self._redis_client.zunionstore, destination, numkeys,
                       key, weight, aggregate)